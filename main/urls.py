from django.urls import path
from .views import CustomRegistrationView, CustomLoginView, custom_logout, index, add_comment, delete_comment,comments_view, edit_comment

urlpatterns = [
    path('', index, name='index'),
    path('register/', CustomRegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('add_comment/', add_comment, name='add_comment'),
    path('comments/', comments_view, name='comments'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
]

