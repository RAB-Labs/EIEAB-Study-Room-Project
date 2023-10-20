from django.shortcuts import render


def home(request):
    return render(request, 'landing.html')


def floor1_view(request):
    return render(request, 'floor1RoomSelect.html')

def floor2_view(request):
    return render(request, 'floor2roomselect.html')