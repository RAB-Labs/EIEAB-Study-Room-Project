from django.shortcuts import render


def home(request):
    return render(request, 'landing.html')


def room1(request):
    return render(request, "Room1Template.html")
def floor1_view(request):
    return render(request, 'floor1RoomSelect.html')

def room2(request):
    return render(request, 'Room2Template.html')

def floor2_view(request):
    return render(request, 'floor2RoomSelect.html')

def room3(request):
    return render(request,'Room3Template.html')
def floor3_view(request):
    return render(request,'floor3RoomSelect.html')

def reserve_view(request):
    return render(request,'BookingDetails.html')

