from django.contrib import admin
from django.urls import path, include
from .views import ViewBook, BookList, AboutPage, DetailsBook, CreateBook

urlpatterns = [
    path('book_list', BookList.as_view(), name='book'),
    path('book/<int:pk>/', DetailsBook.as_view(), name='det_book'),
    path('create_book/', CreateBook.as_view(), name='create_book'),
]
