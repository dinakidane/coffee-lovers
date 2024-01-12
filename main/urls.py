from django.urls import path
from .views import CustomRegistrationView, CustomLoginView, custom_logout, index, add_comment

urlpatterns = [
    path('', index, name='index'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('add_comment/', add_comment, name='add_comment'),
]

