from django.shortcuts import render


def home(request):
    return render(request, 'Landing-page.html')
