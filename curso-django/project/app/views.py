from django.shortcuts import render
from .models import Car

def my_view(request):
    car_list = Car.objects.all()
    context = {
        "car_list": car_list
    }
    return render(request=request,template_name="app/car_list.html", context=context)
