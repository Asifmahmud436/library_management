from django.shortcuts import render,redirect
from books.models import Book
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.views.generic import DetailView
from books.forms import ReviewForm
# Create your views here.


class DetailsBookView(DetailView):
    model = Book
    pk_url_kwarg = 'id'
    template_name = 'book_details.html'
    
    def post(self,request,*args,**kwargs):
        review_form = ReviewForm(data=self.request.POST)
        book = self.get_object() 
        if review_form.is_valid():
            review_form.instance.account = request.user
            new_review = review_form.save(commit=False)
            new_review.book = book
            # new_review.instance.account = request.user
            new_review.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        reviews = book.reviews.all()
        review_form = ReviewForm()

        context['reviews'] = reviews
        context['review_form'] = review_form
        return context
    
def borrowBook(request,id):
    book = Book.objects.get(pk=id)
    if book.price < request.user.account.balance:
        book.borrowed_by = request.user
        request.user.account.balance -= book.price
        request.user.account.save(update_fields=['balance'])
        book.save(update_fields=['borrowed_by'])
    return redirect('home')

def returnBook(request,id):
    book = Book.objects.get(pk=id)
    book.borrowed_by = None
    request.user.account.balance += book.price
    request.user.account.save(update_fields=['balance'])
    book.save(update_fields=['borrowed_by'])
    return redirect('home')