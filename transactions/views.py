from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from transactions.forms import DepositForm
# Create your views here.
def send_transacation_email(user,amount,subject,template):
    message = render_to_string(template,{
        'user' : user,
        'amount' : amount,
    })
    send_email = EmailMultiAlternatives(subject,'',to=[user.email])
    send_email.attach_alternative(message,'text/html')
    send_email.send()


def depositView(request):
    deposited_amount = None
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            form.instance.account = request.user
            form.instance.deposited_balance = form.cleaned_data['deposited_balance']
            deposited_amount = form.cleaned_data['deposited_balance']
            # deposited_amount = form.cleaned_data['balance']
            amount = request.user.account
            amount.balance += deposited_amount
            request.user.account.save(update_fields=['balance'])
            # request.user.account.balance = amount
            # print(request.user.account.balance)
            form.save()
            send_transacation_email(request.user,deposited_amount,"Deposit Message",'deposit_email.html')
            return redirect('profile')
    else:
        form = DepositForm()
    return render(request,'deposit_form.html',{'form':form})

