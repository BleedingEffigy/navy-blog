from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login
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
