from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, status
from rest_framework.throttling import UserRateThrottle
from django_filters import rest_framework as filters
import json

from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer, UserSerializer

# Custom Token Serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# User Registration
@api_view(['POST'])
def register_user(request):
    print('User registration request:', request.data)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('User registered:', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    print('User registration failed:', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Filter for Books
class BookFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')
    category = filters.NumberFilter(field_name='category__id')
    published_year = filters.NumberFilter(field_name='published_date__year')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'category', 'published_year', 'title']

# Book ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]
    filterset_class = BookFilter
    pagination_class = None

    def create(self, request, *args, **kwargs):
        print("Creating book with data:", request.data)
        return super().create(request, *args, **kwargs)


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle]

    def list(self, request, *args, **kwargs):
        print('Fetching category list')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print('Creating category:', request.data)
        return super().create(request, *args, **kwargs)

# Get list of users (for debugging)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.all().values('id', 'username')
    return Response(users)
