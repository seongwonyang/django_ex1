from django.contrib import admin
from bookstore.models import Bookstore
# Register your models here.

class BookstoreAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'author','price', 'url')

admin.site.register(Bookstore)
