from django.urls import path
from . import views
from .views import index, add_comment

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('add_comment/', add_comment, name='add_comment'),
]
