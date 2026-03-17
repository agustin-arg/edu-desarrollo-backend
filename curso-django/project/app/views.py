from django.shortcuts import render

def my_view(request):
    car_list = [
    {"title": "BMW"},
    {"title": "Mazda"},
    {"title": "Toyota"},
    {"title": "Honda"},
    {"title": "Ford"},
    {"title": "Mercedes-Benz"},
    {"title": "Audi"},
    {"title": "Volkswagen"},
    {"title": "Nissan"},
    {"title": "Chevrolet"}
    ]
    context = {
        "car_list": car_list
    }
    return render(request=request,template_name="app/car_list.html", context=context)
