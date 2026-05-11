from django.urls import path
from . import views

#2 punto de entrada y acana se manejan todas las rutas (url) de esta aplicacion

urlpatterns = [
path('', views.index, name='home_productos'),
path('longin/', views.longin, name='home_productos'),
path('register/', views.register, name='home_productos'),
path('dashboard/', views.dashboard, name='home_productos'),
path('venta/', views.venta, name='home_productos'),
path('cervezas/', views.lista_cervezas, name='cervezas'),
]