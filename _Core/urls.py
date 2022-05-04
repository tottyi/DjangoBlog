from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import routers
from Chat import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.ApiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Chat.urls')),
    path('', include(router.urls)),
    path('accounts/', include("django.contrib.auth.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]