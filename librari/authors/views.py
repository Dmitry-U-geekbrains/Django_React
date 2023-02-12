from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, User, Book, Article, Biography
from .serializers import AuthorModelSerializer, UserModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithFullName
from .serializers import AuthorSerializer, AuthorSerializerBase, BookSerializer,BookSerializerBase

class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name', 'last_name', 'birthday_year']
    pagination_class = AuthorPaginator

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


class MyAPIView(APIView):

    def get(self, request):
        return Response({'data': 'GET SUCCESS'})

    def post(self, request):
        return Response({'data': 'POST SUCCESS'})


class MyAPIView(CreateAPIView, ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class MyAPIView(ViewSet):
    def list(self, request,):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)


@action(detail=False, methods=['get'])
def blablabla(self, request):
    return Response({'data': 'DATA'})


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserSerializerWithFullName
        return UserSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return AuthorSerializerBase
        return AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BookSerializer
        return BookSerializerBase