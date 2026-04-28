from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
# router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'blogs', views.BlogPostViewSet,  basename='blogs')

urlpatterns = [
    path(r'', include(router.urls)),
    # path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
