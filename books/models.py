from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='books/media/upload')
    category = models.ManyToManyField(Category)
    borrowed_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name ='reviews')
    body = models.TextField(blank=True,null=True)
    account = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)

    def __str__(self):
        return f'Reviews on {self.book.title}'
