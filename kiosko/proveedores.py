from kiosko.excelfIle import readFileSheet
import pandas as pd
import openpyxl
from django.conf import settings
from openpyxl.styles import NamedStyle
from openpyxl import Workbook
from kiosko.helper import Helpers


class Proveedores:
    def __init__(self):
        pass

    def sheet_proveedores(self):
        contenidoproveedores =readFileSheet("Proveedor")
    
        return contenidoproveedores


    def guadar_proveedor(self,id, nombre, telefono):
        try:
            with pd.ExcelWriter(settings.NEGOCIO_DB,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                helper= Helpers()
                IDpagos = helper.setear_id(writer,"Productos", id)
                id_ = IDpagos
                df=pd.DataFrame({'ID' : id_, 'Nombre': [nombre], 'Telefono': [telefono] })

                if id == '':
                    df.to_excel(writer, float_format=None, sheet_name="Proveedor",header=None, startrow=writer.sheets["Proveedor"].max_row,index=False)
                else:
                    df.to_excel(writer, sheet_name="Proveedor",header=None, startrow=int(id) ,index=False)
        except ValueError:
            print(ValueError)  