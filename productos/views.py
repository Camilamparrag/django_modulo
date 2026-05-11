from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Cerveza



# Create your views here.
def index(request):
    productos = Producto.objects.all() #trae los productos desde la db 
    return render(request, "productos/home.html", {"productos":productos})

def lista_cervezas(request):
    cervezas = Cerveza.objects.all()
    return render(request,"beer/beer.html", {'cervezas':cervezas})    

def dashboard(request):
    return HttpResponse("dashboard")

def register(request):
    return HttpResponse("register")

def venta(request):
    return HttpResponse("venta")

def longin(request):
    return HttpResponse("longin")
