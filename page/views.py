from django.shortcuts import render
from .models import Book
from django.views.generic import CreateView, ListView, DetailView, TemplateView


class ViewBook(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'book_list'


class BookList(ListView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book_list'


class AboutPage(TemplateView):
    template_name = 'about.html'


class DetailsBook(DetailView):
    model = Book
    template_name = 'details_book.html'
    context_object_name = 'det_book'


class CreateBook(CreateView):
    model = Book
    template_name = 'create_book.html'
    fields = ['name_book', 'author', 'number_pages', 'price', 'image']
