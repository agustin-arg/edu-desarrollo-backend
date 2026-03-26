from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Car


def my_view(request):
    car_list = Car.objects.all()
    context = {"car_list": car_list}
    return render(request=request, template_name="app/car_list.html", context=context)


def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")


class CarListView(TemplateView):
    template_name = "app/car_list.html"

    def get_context_data(self, **kwargs):
        car_list = Car.objects.all()
        return {"car_list": car_list}
