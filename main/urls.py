from django.urls import path
from .views import CustomRegistrationView, CustomLoginView, custom_logout, index, add_comment, delete_comment, add_reply

urlpatterns = [
    path('', index, name='index'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('add_comment/', add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('add_reply/<int:comment_id>/', add_reply, name='add_reply'), 
]

