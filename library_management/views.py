from django.shortcuts import render,redirect
from books.models import Book
from categories.models import Category
def home(request,category_slug=None):
    data = Book.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Book.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request,'home.html',{'data':data,'category':categories})

def show_books(request):
    books = Book.objects.filter(borrowed_by=request.user)
    # print(data.cleaned_data)
    return render(request,'show_books.html',{'books':books})