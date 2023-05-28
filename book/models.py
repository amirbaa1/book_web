from django.db import models
from django.urls import reverse


class Book(models.Model):
    name_book = models.CharField(max_length=30)
    author = models.CharField(max_length=60)
    number_pages = models.IntegerField()
    price = models.IntegerField()
    text = models.TextField(max_length=300, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/%y")

    def __str__(self):
        return f"{self.name_book}"

    def get_absolute_url(self):
        return reverse('det_book', args=[str(self.id)])
