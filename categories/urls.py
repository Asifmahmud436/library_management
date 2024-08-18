from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('add_categories/',views.add_categories)
]