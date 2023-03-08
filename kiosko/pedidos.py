from kiosko.excelfIle import readFileSheet
import pandas as pd
from pandas import DataFrame
import numpy as np
from django.conf import settings
from kiosko.helper import Helpers


class Pedidos:
    def __init__(self):
        pass

    def sheet_pedidos(self):
        contenidopedidos =readFileSheet("Pedidos")
    
        return contenidopedidos

    def traer_proveedor_id(self, id):
        proveedores = readFileSheet("Proveedor")
        query =proveedores.query(f'ID== {id}')
        proveedor = query.to_numpy() 
        return proveedor[0][1]

    def traer_producto_id(self, id):
        productos = readFileSheet("Productos")
        query =productos.query(f'ID== {id}')
        producto = query.to_numpy() 
        return producto[0][1]

    def guardar_pedidos(self,id,fecha, cantidad, producto, recibido, pago, mediodepago, monto, parcial, proveedor):
        try:
            nombreproducto = self.traer_producto_id(producto)
            nombreproveedor = self.traer_proveedor_id(proveedor)
            with pd.ExcelWriter(settings.NEGOCIO_DB,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                helper= Helpers()
                nuevafecha = helper.setear_fecha(fecha)
                IDpagos = helper.setear_id(writer,"Pedidos", id)
                id_ = IDpagos
                df=pd.DataFrame({'ID': id_,'Fecha': [nuevafecha], 'Cantidad': cantidad, 'Producto': nombreproducto, 'Recibido':recibido, 'Pago':pago, 'Medio de Pago':mediodepago, 'Monto':monto, 'Parcial':parcial,'Deuda':None, 'Proveedor':nombreproveedor})
                
                if id == '':
                    df.to_excel(writer, sheet_name="Pedidos",float_format="",header=None, startrow=writer.sheets["Pedidos"].max_row,index=False)
                else:
                    df.to_excel(writer, sheet_name="Pedidos",float_format='%f',header=None, startrow=int(id) ,index=False)

        except ValueError:
            print(ValueError)  