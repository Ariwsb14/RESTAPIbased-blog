from rest_framework import viewsets
from blog.models import Post,Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter
from .paginations import PostPaginator

class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    permission_classes =[IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend , SearchFilter,OrderingFilter]
    filterset_fields = ['category', 'author','status']
    search_fields = ['title','content']
    ordering_fields = ['published_date']
    pagination_class = PostPaginator

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes =[IsAuthenticatedOrReadOnly , IsOwnerOrReadOnly]
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]