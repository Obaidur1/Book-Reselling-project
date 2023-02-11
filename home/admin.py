from django.contrib import admin
from .models import books,Order,TrackUpdate



class BookAdmin(admin.ModelAdmin):
     list_display = ('book_name', 'category', 'price', 'pickuplocation')
# Register your models here.
admin.site.register(books,BookAdmin),
admin.site.register(Order),
admin.site.register(TrackUpdate),