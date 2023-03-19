from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, User, Book, Article, Biography


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BiographySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BookleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'