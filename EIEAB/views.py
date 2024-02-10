from django.shortcuts import render
from .models import bookingRoom

roomInfo = bookingRoom()


def home(request):
    return render(request, 'landing.html')


def floor1_view(request):
    roomInfo.floor = '1'
    return render(request, 'floor1RoomSelect.html')


def floor2_view(request):
    roomInfo.floor = '2'
    return render(request, 'floor2RoomSelect.html')


def floor3_view(request):
    roomInfo.floor = '3'
    return render(request, 'floor3RoomSelect.html')


def room1(request):
    roomInfo.room = '1.100'
    return render(request, "Room1Template.html")


def room2(request):
    roomInfo.room = '2.200'
    return render(request, 'Room2Template.html')


def room3(request):
    roomInfo.room = '3.000'
    return render(request, 'Room3Template.html')


def reserve_view(request):
    if request.method == "POST":
        # Other form processing...

        # Capture the booking times from the form
        booking_start = request.POST.get('booking_start')
        booking_end = request.POST.get('booking_end')

        # Process the booking (e.g., save to database)

        # Pass the booking times to the template or handle as needed
        context = {
            'booking_start': booking_start,
            'booking_end': booking_end,
            # Include other context variables as needed
        }
        return render(request, 'BookingDetails.html', context)
