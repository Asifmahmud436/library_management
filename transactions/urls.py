from .import views
from django.urls import path,include

urlpatterns = [
    path('deposit/',views.depositView,name='deposit'),
]