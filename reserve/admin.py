from django.contrib import admin
from .models import Room, Reservation

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price', 'availability', )
    list_filter = ('room_type',)
    


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'days', 'date_from', 'date_to', 'customer_name', 'total_price')
    list_filter = ('date_to', 'date_from',)