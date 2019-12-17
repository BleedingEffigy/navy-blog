from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from blog.models import Comment

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile(request):
    comments = Comment.objects.filter(
        author__username__contains = request.user.username
    ).order_by(
        '-created_on'
    )
    context = {
        'user': request.user,
        'comments': comments
    }
    return render(request, 'profile.html', context)

def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

