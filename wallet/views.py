from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import balance
from .forms import add_money, sendform


def add_bal(request):
    form = add_money(request.POST)
    if form.is_valid():
        bale = form.cleaned_data['amount']
        bal = balance.objects.get(WUser=request.user)
        bal.balance += bale
        print(bale)
        bal.save()
        return redirect('/user/')

    else:
        form = add_money()
    return render(request, 'add.html', {'form': form})


def send(request):
    form = sendform(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        amount = form.cleaned_data['amount']
        remark = form.cleaned_data['remark']
        if User.objects.filter(username=username).exists():
            var = balance.objects.get(WUser=request.user)
            var.balance = var.balance-amount
            var.save()
            var1=User.objects.get(username=username)
            var2 = balance.objects.get(WUser=var1)
            var2.balance=var2.balance+amount
            var2.save()
        else:
            print("uer does not exist")
    return render(request, 'transfer.html', {"form": form})
