from django.db import models


# Create your models here.
class Room(models.Model):
    # Integer
    ROOM_OPTIONS = (
        ('Executive', 'Executive Room'),
        ('Standard', 'Standard Room'),
        ('Villa', 'Villa Room'),
        ('Double', 'Double Room'),
    )
    room_number = models.IntegerField()
    availability = models.BooleanField(default=True)
    room_type = models.CharField(max_length=200, choices=ROOM_OPTIONS)
    price = models.IntegerField()
#  Need edit Picture
    room_picture = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100)

    
    def __str__(self):
        return str(self.room_number) + self.room_type

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    date_from = models.DateField()
    date_to = models.DateField()
    days = models.IntegerField(default=1)
    total_price = models.IntegerField()
    room_type = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_number = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name + "\'s reservation"
