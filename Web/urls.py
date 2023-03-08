"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from kiosko.views import *
# ver autenticacion 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login , name='login'),
    path("authenticate",authenticate),
    path('index',index ,name='index'),

    path('ventas', ventas_form ,name='ventas'),
    path('ventas/id_venta<int:num>',ventas_form ,name='ventas'),
    path('editarGuadarVentas',editarGuadarVentas),


    path('pedidos',pedidos ,name='pedidos'),
    path('pedidos/id_pedido<int:num>',pedidos ,name='pedidos'),
    path('EditarGuadarPedidos', guardar_pedido),

    path('productos',productos ,name='productos'),
    path('productos/id_producto<int:num>',productos ,name='productos'),
    path('EditarGuadarProductos', EditarGuadarProductos),
    
    path('pagos', pagos ,name='pagos'),
    path('pagos/id_pago<int:num>',pagos ,name='pagos'),
    path('editarGuadarPagos',editarGuadarPagos),


    path('proveedores', proveedores ,name='proveedores'),
    path('proveedores/id_proveedores<int:num>',proveedores ,name='proveedores'),
    path('editarGuadarProveedores',editarGuadarProveedores),


    path('reportes', reportes, name='reportes'),
    
    path('logout', logout, name='logout')

]
