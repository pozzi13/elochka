from django.contrib import admin

from .models import Booking, Review


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'phone', 'service')
    list_filter = ('service', 'created_at')
    search_fields = ('name', 'phone')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'rating', 'is_published')
    list_filter = ('is_published', 'rating', 'created_at')
    search_fields = ('name', 'text')
    list_editable = ('is_published',)
