from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from .models import Product


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("list_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductTableView(generic.ListView):
    model = Product
    template_name = "products/table_product.html"
    context_object_name = "products"

class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"