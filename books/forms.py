# from books.models import Book
from django import forms
from books.models import Review

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body']