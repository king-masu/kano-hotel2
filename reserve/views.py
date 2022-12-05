from django.shortcuts import render, get_object_or_404, redirect
from .models import Room
from .forms import ReservationForm
from django.contrib import messages


# Create your views here.
def available_rooms(request):
    available_rooms = Room.objects.filter(availability = True)
    
    return render(request, 'reserve/available_rooms.html', {'available_rooms':available_rooms})

def reserve_room(request, pk):
  room = get_object_or_404(Room, pk=pk)
  if request.method == "POST":
    reservation_form = ReservationForm(request.POST)
    if reservation_form.is_valid():
        new_reservation = reservation_form.save(commit=False)
        # if room.availability = False:
        #       return render(request, 'reserve/reserve_success.html', {'reservation_code': reservation_code})

        new_reservation.room = room
        new_reservation.room_type = room.room_type
        new_reservation.total_price = new_reservation.days * room.price
        new_reservation.save()
        # reservation_form.save()
        reservation_code = new_reservation.pk
        room.availability = False
        room.price = 300
        room.save()
        return render(request, 'reserve/reserve_success.html', {'reservation_code': reservation_code})
    else:
        messages.error(request, 'Error MAKING RESERVATION, TRY AGAIN')

    # SOMETHING VBETTER FOR THIS REDIRECT
    return redirect("reserve:available_rooms")

  form = ReservationForm()
  return render(request, 'reserve/reserve_room.html', {'room':room, 'form': form})
	# return render(request=request, template_name="main/home.html", context={'movie_form':movie_form, 'movies':movies})