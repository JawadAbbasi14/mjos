from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from .forms import Signupform, Feedback_form


def _account_redirect_url(request):
    next_url = request.POST.get("next") or request.GET.get("next")
    if next_url and url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        return next_url
    return "dashboard"


def signup_views(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
        
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(_account_redirect_url(request))
    else:
        form = Signupform()
    next_url = request.POST.get("next") or request.GET.get("next", "")
    return render(request, "accounts/signup.html", {"form": form, "next": next_url})


def login_views(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
        
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(_account_redirect_url(request))
    else:
        form = AuthenticationForm()
    next_url = request.POST.get("next") or request.GET.get("next", "")
    return render(request, "accounts/login.html", {"form": form, "next": next_url})


@login_required(login_url='login')
def dashboard(request):
    return render(request, "accounts/dashboard.html")



@require_POST
def logout_views(request):
    logout(request)
    return redirect("home")


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