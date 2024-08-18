from .import views
from django.urls import path,include

urlpatterns = [
    path('register/', views.register,name='register'),
    path('sign_in/', views.sign_in,name='sign_in'),
    path('sign_out/', views.sign_out,name='sign_out'),
    path('profile/', views.profile,name='profile'),
]