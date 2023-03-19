from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, UserModelViewSet, ArticleModelViewSet, BiographyModelViewSet, BookModelViewSet, MyAPIView, UserListAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('users', UserModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('book', BookModelViewSet)
# router.register('my', MyAPIView, basename='my')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    # path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view({'get': 'list'})),
    # re_path(r'^api/(?P<version>\d\.\d)/users/$', UserListAPIView.as_view()),
    # path('api/users/0.1', include('userapp.urls', namespace='0.1')),
    # path('api/users/0.2', include('userapp.urls', namespace='0.2')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]


