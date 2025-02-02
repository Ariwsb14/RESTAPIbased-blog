from rest_framework import viewsets
from blog.models import Post,Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CategorySerializer

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer