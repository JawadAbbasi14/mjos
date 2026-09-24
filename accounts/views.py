from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Signupform, Feedback_form

def signup_views(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
        
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = Signupform()
    return render(request, "accounts/signup.html", {"form": form})


def login_views(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
        
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required(login_url='login')
def dashboard(request):
    return render(request, "accounts/dashboard.html")


def logout_views(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def feedback_views(request):
    if request.method == "POST":
        feedback = Feedback_form(request.POST)
        if feedback.is_valid():
            feedback_instance = feedback.save(commit=False)
            if hasattr(feedback_instance, 'user') and not feedback_instance.user_id:
                feedback_instance.user = request.user
            feedback_instance.save()
            return redirect("dashboard")
    else:
        feedback = Feedback_form()
    return render(request, "accounts/feedback.html", {"feedback_form": feedback})