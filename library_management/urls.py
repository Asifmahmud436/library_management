from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('show_books/', views.show_books,name='show_books'),
    path('transactions/', include('transactions.urls')),
    path('categories/', include('categories.urls')),
    path('category/<slug:category_slug>/', views.home,name='category_wise_post'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)