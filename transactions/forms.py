from django import forms
from django.contrib.auth.models import User
from transactions.models import Transaction
class DepositForm(forms.ModelForm):
    deposited_balance = forms.IntegerField(label="Deposit")
    class Meta:
        model = Transaction
        fields = ['deposited_balance']