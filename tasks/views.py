from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "tasks/signup.html", {"form": form})

@login_required
def home():
    pass