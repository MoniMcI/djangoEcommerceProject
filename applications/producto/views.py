from django.shortcuts import render,get_object_or_404

#
from django.db.models import Q

# Create your views here.

from django.views.generic import ListView, DetailView

from .models import Producto

class ProductoListView(ListView):
    model = Producto
    paginate_by = 2 
    template_name = 'producto/productos.html'
    ordering= 'nombre_prod'

    def get_context_data(self, **kwargs):
        productos = Producto.objects.all()
        context = super(ProductoListView,self).get_context_data(**kwargs)
        context['productos'] = productos
        return context

class productoPorCategoria(ListView):
    template_name= "producto/productos.html"
    paginate_by: 2

    def get_queryset(self):
        slugRecuperado = self.kwargs['categoria_slug']
        listaFiltrada = Producto.objects.filter(
            categoria__categoria_slug=slugRecuperado
        )
        return listaFiltrada

class buscarProducto(ListView):
    model = Producto
    template_name= "producto/productos.html"
    paginate_by: 2
    ordering= 'nombre_prod'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        resultado = Producto.objects.filter(
            Q(nombre_prod__icontains = palabra_clave)|Q(descripcion__icontains = palabra_clave))
        return resultado

class detalleProducto(DetailView):
    model = Producto
    template_name= "producto/detalleProducto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalle'] = self.get_object()
        return context

