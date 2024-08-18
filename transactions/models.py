from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    deposited_balance = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.account.username}'
