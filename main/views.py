from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from django.contrib.auth.views import RegistrationView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html')

def login_view(request):
    # Implement login logic here
    return render(request, 'login.html')

def logout_view(request):
    # Implement logout logic here
    return redirect('index')

def register(request):
    # Implement registration logic here
    return render(request, 'register.html')


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
            return redirect('index')
    else:
        form = CommentForm()

    return render(request, 'index.html', {'form': form})

class CustomRegistrationView(RegistrationView):
    success_url = reverse_lazy('index.html')  # Redirect to the homepage after successful registration

    def register(self, form):
        response = super().register(form)
        # You can add additional logic here if needed
        return response

