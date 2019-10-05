from django import forms

from .models import balance


class add_money(forms.Form):
    amount = forms.IntegerField()
    remark = forms.CharField(max_length=30)

class sendform(forms.Form):
    username=forms.CharField(max_length=255)
    amount=forms.IntegerField()
    remark=forms.CharField(max_length=255)