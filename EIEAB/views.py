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
    room_value = roomInfo.room
    roomval, created = bookingRoom.objects.get_or_create(room=room_value)
    if created:
        roomInfo.save()
    return render(request, 'BookingDetails.html', {'roomInfo': roomInfo})
