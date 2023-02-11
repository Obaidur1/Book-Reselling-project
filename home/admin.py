from django.contrib import admin
from .models import books,Order,TrackUpdate



class BookAdmin(admin.ModelAdmin):
     list_display = ('book_name', 'category', 'price', 'pickuplocation')

class OrderAdmin(admin.ModelAdmin):
     list_display = ('order_id','name','email','address','phone')
# Register your models here.
admin.site.register(books,BookAdmin),
admin.site.register(Order,OrderAdmin),
admin.site.register(TrackUpdate),