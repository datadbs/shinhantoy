from django.contrib import admin
from .models import Order, Comment
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class OrderAdmin(admin.ModelAdmin):
    pass