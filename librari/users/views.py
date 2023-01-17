from rest_framework.viewsets import ModelViewSet
from .models import users
from .serializers import UserModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Usser.objects.all()
    serializer_class = UserModelSerializer
