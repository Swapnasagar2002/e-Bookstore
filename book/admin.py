from django.contrib import admin
from book.models import Category,Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','price', 'is_available')
    search_fields =('title',)
    list_editable =('is_available',)
    list_filter =('is_available','category')
# Register your models here.
admin.site.register(Category)
admin.site.register(Book,BookAdmin)