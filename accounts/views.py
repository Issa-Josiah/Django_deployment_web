from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from django.views.decorators.http import require_POST


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in user immediately after signup
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def home(request):
    return render(request, 'home.html')
