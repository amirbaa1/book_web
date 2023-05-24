from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from django.views.generic import CreateView, ListView, DetailView, TemplateView, UpdateView, DeleteView


# class ViewBook(ListView):
#     model = Book
#     template_name = 'home.html'
#     context_object_name = 'book_view'


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
    context_object_name = 'create_book'


class UpdateBook(UpdateView):
    model = Book
    template_name = 'update_book.html'
    fields = '__all__'
    context_object_name = 'up_book'


class DeleteBook(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('home')
    context_object_name = 'delete'
