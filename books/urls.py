from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('details/<int:id>',views.DetailsBookView.as_view(),name='book_details'),
    path('borrow/<int:id>',views.borrowBook,name='borrow'),
    path('return/<int:id>',views.returnBook,name='return'),
]