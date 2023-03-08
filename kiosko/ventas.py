from kiosko.excelfIle import readFileSheet
import pandas as pd
import openpyxl
from django.conf import settings
from openpyxl.styles import NamedStyle
from openpyxl import Workbook
from kiosko.helper import Helpers


class Ventas:
    def __init__(self):
        pass

    def sheet_reportes_ventas(self):
        contenidoreportesventas =readFileSheet("Ventas")
    
        return contenidoreportesventas

    def guadar_ventas(self,id, fecha, producto, cantidad):
        try:

            with pd.ExcelWriter(settings.NEGOCIO_DB,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                helper= Helpers()
                nuevafecha = helper.setear_fecha(fecha)
                IDpagos = helper.setear_id(writer,"Ventas", id)
                id_ = IDpagos
                df=pd.DataFrame({'ID': id_, 'Fecha': [nuevafecha] , 'Producto': producto, 'Cantidad': cantidad})

                if id == '':
                    df.to_excel(writer, float_format=None, sheet_name="Ventas",header=None, startrow=writer.sheets["Ventas"].max_row,index=False)
                else:
                    df.to_excel(writer, sheet_name="Ventas",header=None, startrow=int(id) ,index=False)
        except ValueError:
            print(ValueError)   
