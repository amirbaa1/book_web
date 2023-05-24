from django.contrib import admin
from django.urls import path, include
from .views import BookList, AboutPage, DetailsBook, CreateBook, UpdateBook, DeleteBook

urlpatterns = [
    path('book_list', BookList.as_view(), name='book'),
    path('book/<int:pk>/', DetailsBook.as_view(), name='det_book'),
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('<int:pk>/edit/', UpdateBook.as_view(), name='update_book'),
    path('book/<int:pk>/delete/', DeleteBook.as_view(), name='delete_book'),
]
