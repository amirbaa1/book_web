from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from book.models import Book


class HomePage(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'book_view'
    ordering = ['-id']


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContactUsPage(TemplateView):
    template_name = 'contact_us.html'
