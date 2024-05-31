from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment

def comments_view(request):
    comments = Comment.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'comments.html', {'comments': comments})

def index(request):
    comments = Comment.objects.all()
    form = CommentForm()
    return render(request, 'index.html', {'comments': comments, 'form': form})

@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comments')
    else:
        form = CommentForm()
    return render(request, 'index.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user.is_authenticated and (request.user.is_staff or request.user == comment.user):
        comment.delete()
    return redirect('comments')

class CustomRegistrationView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('index')
        return render(request, self.template_name, {'form': form})

class CustomLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        return render(request, self.template_name, {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect('index')



