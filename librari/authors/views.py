from rest_framework.viewsets import ModelViewSet
from .models import Author, User
from .serializers import AuthorModelSerializer, UserModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer
from rest_framework.views import APIView, Response


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


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
