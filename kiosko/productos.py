from kiosko.excelfIle import readFileSheet
import pandas as pd
from pandas import DataFrame
import numpy as np
from django.conf import settings
from kiosko.helper import Helpers
import math


class Productos:
    def __init__(self):
        pass

    def sheet_productos(self):
        contenidoproductos =readFileSheet("Productos")
    
        return contenidoproductos


    def guadar_productos(self,id,  nombre, preciocompra ,ganancia, unidades):
       try:

            with pd.ExcelWriter(settings.NEGOCIO_DB,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                helper= Helpers()
                IDpagos = helper.setear_id(writer,"Productos", id)
                id_ = IDpagos
                preciodeventa = int(preciocompra)//100*(int(ganancia))//int(unidades)
                df=pd.DataFrame({'ID': id_,'Nombre': [nombre],'Precio de Compra': preciocompra,'Precio de Venta': preciodeventa,'P de ganancia': ganancia, 'Unidades': unidades})

                if id == '':
                    df.to_excel(writer, sheet_name="Productos",header=None, startrow=writer.sheets["Productos"].max_row,index=False, float_format="")
                else:
                    df.to_excel(writer, sheet_name="Productos",header=None, startrow=int(id) ,index=False)

       except ValueError:
            print(ValueError) 
    