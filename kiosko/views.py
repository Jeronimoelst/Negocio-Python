from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from kiosko.users import Users
from kiosko.pedidos import Pedidos
from kiosko.productos import Productos
from kiosko.pagos import Pagos
from kiosko.reportes import Reportes
from kiosko.proveedores import Proveedores
from kiosko.ventas import Ventas



# Create your views here.
def login(request):
     return render(request, "login.html")

def authenticate(request):   
    userName = request.POST['nombre']
    password = request.POST['password']
    user= Users()
    authenticated = user.isAuthenticated(userName,password)
  
    if authenticated:
        request.session['user_name'] = userName
        request.session['loggedIn'] = True
        return HttpResponseRedirect("index")
    else:    
        context={'message': "Usuario o contraseña incorrectos!"}
        return render(request, "login.html", context)
# 
# 
# 
def logout(request):
    request.session['loggedIn'] = False
    return HttpResponseRedirect("/")
# 
# 
# 
def index(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:    
        usuario = request.session['user_name']
        contexto = {"usuario": usuario}
        return render(request, "index.html", contexto)
    else:
        return HttpResponseRedirect("/")  
# 
# 
# 

def ventas_form(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:  
        if 'id_venta' in request.GET:
            ventas = Ventas()
            venta = ventas.sheet_reportes_ventas()
            idventa = request.GET['id_venta']
            query =venta.query(f'ID== {idventa}')
            desc = query.to_numpy()
        else:
            desc = ""
        contexto = {"venta" : desc}
        return render(request, "ventas.html",contexto)
    else:
        return HttpResponseRedirect("/") 

def editarGuadarVentas(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:     
        id = request.POST['id']   
        fecha = request.POST['fecha']
        producto = request.POST['producto']
        cantidad = request.POST['cantidad']
        ventasnuevas = Ventas()
        ventasnuevas.guadar_ventas(id, fecha, producto, cantidad)
        return HttpResponseRedirect("/ventas")
    else:
        return HttpResponseRedirect("/")    

#    
# 
# 
def pedidos(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:
        ordenes = Pedidos()
        pedidos=ordenes.sheet_pedidos()
        pedidos = pedidos.sort_values(by='ID',ascending=False)
        if 'id_pedido' in request.GET:
            idpedido = request.GET['id_pedido']
            query =pedidos.query(f'ID== {idpedido}')
            pedido = query.to_numpy()
        else:
            pedido = ""
        productos = Productos()
        articulos = productos.sheet_productos()
        informes = Reportes()
        proveedores = informes.sheet_reportes_proveedor()
        contexto = {"pedidos": pedidos.itertuples(), "articulos": articulos.itertuples(index=False), "proveedores": proveedores.itertuples(index=False), "pedido" : pedido}
        return render(request, "pedidos.html", contexto)
    else:
        return HttpResponseRedirect("/")   

def guardar_pedido(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:
        id = request.POST['id']         
        fecha = request.POST['fecha']
        cantidad = request.POST['cantidad']
        producto = request.POST['producto']
        recibido = request.POST['recibido']
        pago = request.POST['pago']
        mediodepago = request.POST['medio_de_pago']
        monto = request.POST['monto']
        parcial = request.POST['parcial']
        proveedor = request.POST['proveedor']
        pedidosnuevos = Pedidos()
        pedidosnuevos.guardar_pedidos(id,fecha, cantidad, producto, recibido, pago, mediodepago, monto, parcial, proveedor)
        return HttpResponseRedirect("/pedidos")
    else:
        return HttpResponseRedirect("/")   

# 
# 
# 
def productos(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:        
        productos = Productos()
        articulos = productos.sheet_productos()
        articulos = articulos.sort_values(by='ID',ascending=False)
        if 'id_producto' in request.GET:
            idproducto = request.GET['id_producto']
            query =articulos.query(f'ID== {idproducto}')
            articulo = query.to_numpy()
        else:
            articulo = ""
        contexto = {"articulos": articulos.itertuples(), "articulo" : articulo}
        return render(request, "productos.html", contexto)
    else:
        return HttpResponseRedirect("/")  

def EditarGuadarProductos(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']: 
        id = request.POST['id']
        nombre = request.POST['nombre']
        preciocompra = request.POST['precio_compra']
        ganancia = request.POST['ganancia']
        unidades = request.POST['unidades']
        cargaproductos = Productos()
        cargaproductos.guadar_productos(id, nombre, preciocompra ,ganancia, unidades)
        return HttpResponseRedirect("/productos")
    else:
        return HttpResponseRedirect("/")
# 
# 
# 
def pagos(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:        
        rendecion = Pagos()
        pago = rendecion.sheet_pagos()
        pago = pago.sort_values(by='ID',ascending=False)
        if 'id_pago' in request.GET:
            idpago = request.GET['id_pago']
            query =pago.query(f'ID== {idpago}')
            rendecion = query.to_numpy()
        else:
            rendecion = ""
        contexto = {"pagos": pago.itertuples(), "rendecion" : rendecion}
        return render(request, "pagos.html", contexto)
    else:
        return HttpResponseRedirect("/")    

def editarGuadarPagos(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:     
        id = request.POST['id']   
        monto = request.POST['monto']
        fecha = request.POST['fecha']
        concepto = request.POST['concepto']
        pagosnuevos = Pagos()
        pagosnuevos.guadar_pagos(id,monto, fecha, concepto)
        return HttpResponseRedirect("/pagos")
    else:
        return HttpResponseRedirect("/")    
   
# 
# 
# 
def proveedores(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:        
        proveedores = Proveedores()
        proveedor_ = proveedores.sheet_proveedores()
        proveedor_ = proveedor_.sort_values(by='ID',ascending=False)
        if 'id_proveedor' in request.GET:
            id_proveedor = request.GET['id_proveedor']
            query =proveedor_.query(f'ID== {id_proveedor}')
            proveedor = query.to_numpy()
        else:
            proveedor = ""
        contexto = {"proveedores": proveedor_.itertuples(), "proveedor" : proveedor}
        return render(request, "proveedores.html", contexto)
    else:
        return HttpResponseRedirect("/")    

def editarGuadarProveedores(request):

    if request.session['loggedIn'] is not None and request.session['loggedIn']:     
        id = request.POST['id']   
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']
        proveedornuevos = Proveedores()
        proveedornuevos.guadar_proveedor(id, nombre, telefono)
        return HttpResponseRedirect("/proveedores")
    else:
        return HttpResponseRedirect("/")    
   



# 
# 
# 
def reportes(request):
    if request.session['loggedIn'] is not None and request.session['loggedIn']:  
        informes = Reportes()
        ventas = informes.sheet_reportes_ventas()
        registros = informes.sheet_reportes_registro()
        ganancias = informes.sheet_reportes_ganancias()
        gastos = informes.sheet_reportes_gastos()
        turnos = informes.sheet_reportes_turnos()
        contexto = { "ventas":ventas.itertuples(index=False) ,"registros":registros.itertuples(index=False)}
        return render(request, "reportes.html", contexto)
    else:
        return HttpResponseRedirect("/")    
