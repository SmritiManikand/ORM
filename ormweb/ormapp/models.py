from django.db import models
from django.contrib import admin
class Book(models.Model):
    author_name=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    publication_date=models.DateField()
    ISBN=models.CharField(max_length=13,unique=True)
    description=models.TextField()
class BookAdmin(admin.ModelAdmin):
    list_display=("author_name","title","publication_date","ISBN","description")