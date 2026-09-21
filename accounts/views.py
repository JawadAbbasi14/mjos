from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .forms import Signupform,Feedback_form

# Signup function logic
def signup_views(request):
    if request.method == "POST":
        print("Step one done POST")
        form = Signupform(request.POST)


        if form.is_valid():
            print("step 2 done Validity")
            user = form.save()
            login(request, user)
            print("Login sucessfully!")
            return redirect("dashboard")
        print(f"Form error {form.errors}")  # 1. Isay block ke ANDAR hona chahiye
    else:
        form = Signupform()  # GET request ke liye khali form

    # 2. Render se pehle 'return' lagana lazmi hai
    return render(request, "accounts/signup.html", {"form": form})


# Login function logic
def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        # 3. Validation check lagana zaroori hai, iske baghair cleaned_data nahi chalta
        if form.is_valid():
            # 4. Spelled correctly and used '=' instead of '-'
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = AuthenticationForm()  # GET request ke liye khali form

    # 5. Render se pehle 'return' lagaya aur login page ka template use kiya
    return render(request, "accounts/login.html", {"form": form})



# Logic for dashboard

def dashboard(request):
    return render(request,"accounts/dashboard.html")

# Logout logic 

def logout_views(request):
    if request.method == "POST":
        print("Done 1 post requst sucess")
        logout(request)
        print("LOgout ho gya")
        return redirect("login")

    logout(request)
    return redirect("login")


    # for Feedback
def feedback_views(request):
    if request.method == "POST":
        feedback = Feedback_form(request.POST)

        if feedback.is_valid():
           feedback.save()
           return render(request,"accounts/dashboard.html",{"feedback_form":feedback})

        return render(request,"accounts/feedback.html", {"feedback_form":feedback})

    else:
      
        feedback = Feedback_form()
        return render(request, "accounts/feedback.html", {"feedback_form": feedback})

    