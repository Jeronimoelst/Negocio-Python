from kiosko.excelfIle import readFileSheet
import pandas as pd
import openpyxl
from django.conf import settings
from openpyxl.styles import NamedStyle
from openpyxl import Workbook
from kiosko.helper import Helpers


class Pagos:
    def __init__(self):
        pass

    def sheet_pagos(self):
        contenidopagos =readFileSheet("Pagos")
    
        return contenidopagos

    def guadar_pagos(self,id, monto, fecha, concepto):
        try:

            with pd.ExcelWriter(settings.NEGOCIO_DB,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
                helper= Helpers()
                nuevafecha = helper.setear_fecha(fecha)
                IDpagos = helper.setear_id(writer,"Pagos", id)
                id_ = IDpagos
                df=pd.DataFrame({'ID': id_, 'Monto': monto ,'Fecha': [nuevafecha], 'Concepto': concepto})

                if id == '':
                    df.to_excel(writer, float_format=None, sheet_name="Pagos",header=None, startrow=writer.sheets["Pagos"].max_row,index=False)
                else:
                    df.to_excel(writer, sheet_name="Pagos",header=None, startrow=int(id) ,index=False)
        except ValueError:
            print(ValueError)   

