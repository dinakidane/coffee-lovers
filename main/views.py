from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment


def comments_view(request):
    comments = Comment.objects.filter(approved=True).order_by('-created_at')
    form = CommentForm()  # Add the form here
    return render(request, 'comments.html', {'comments': comments, 'form': form})

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
            comment.approved = True  # Automatically approve comments for now
            comment.save()
            print(f"Comment saved: {comment.coffee_experience}")  # Debugging statement
            return redirect('comments')
        else:
            print("Form is not valid")  # Debugging statement

    else:
        form = CommentForm()
    return render(request, 'comments.html', {'form': form})

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
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return render(request, self.template_name, {'form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        return redirect('comments')
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comments')
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'edit_comment.html', {'form': form})

class CustomLoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'You have successfully logged in.')
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return render(request, self.template_name, {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')



