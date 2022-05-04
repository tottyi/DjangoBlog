from django.urls import path
from . import views
from .views import DeletePostView, ApiViewSet

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('blog/', views.blog, name='blog'),
    path("register/", views.register, name="register"),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<int:pk>/remove', DeletePostView.as_view(), name='delete'),
]
