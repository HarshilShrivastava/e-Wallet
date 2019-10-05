
from django.shortcuts import render, redirect
from wallet.models import balance
from django.contrib.auth.forms import UserCreationForm


def index(request):
    bal = balance.objects.get(WUser=request.user)
    return render(request, 'registration/home.html', {"balance": bal.balance})


def Signup(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def Login(request):
    return render(request, 'registration/login.html')


def profile(request):
    return render(request, 'registration/profile.html')
