from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/posts', PostViewSet, basename='post')
router.register(r'api/v1/groups', GroupViewSet, basename='group')
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
