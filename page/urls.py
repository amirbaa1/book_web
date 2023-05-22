from django.contrib import admin
from django.urls import path, include
from .views import ViewBook, BookList, AboutPage, DetailsBook, CreateBook

urlpatterns = [
    path('', ViewBook.as_view(), name='home'),
    path('/book', BookList.as_view(), name='book'),
    path('/about', AboutPage.as_view(), name='about'),
    path('/<int:pk>/', DetailsBook.as_view(), name='det_book'),
    path('/create_book/', CreateBook.as_view(), name='create_book'),
]
