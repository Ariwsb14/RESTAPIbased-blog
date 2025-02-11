from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import (RegistrationsSerializer , CustomAuthTokenSerializer, 
                          CustomTokenObtainPairSerializer ,ChangePasswordSerializer , ProfileAPISerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User , Profile
from django.shortcuts import get_object_or_404

# make your views here

'''
user registration view with email , password, password confirmations(password1)
'''
class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationsSerializer
    def post(self, request, *args, **kwargs):
        serializer = RegistrationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email'],
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Token based login and token generating
'''
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
            }
        )

'''
token based logout and deleting the token of user
'''
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''
creating and login with Jason Web Token.
'''
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=  CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.GenericAPIView):
    serializer_class= ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]
    def get_object(self):
        obj = self.request.user
        return obj
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password':['wrong password']}, status = status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'details': 'password change successfully'} , status = status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileAPISerializer
    queryset = Profile.objects.all()
    def get_object(self):
        query_set = self.get_queryset()
        obj = get_object_or_404(query_set,user=self.request.user)
        return obj