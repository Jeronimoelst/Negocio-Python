from kiosko.excelfIle import readFileSheet
import pandas as pd
from pandas import DataFrame
import numpy as np


class Reportes:
    def __init__(self):
        pass

    def sheet_reportes_proveedor(self):
        contenidoreportesproveedor =readFileSheet("Proveedor")
    
        return contenidoreportesproveedor

    
    def sheet_reportes_ventas(self):
        contenidoreportesventas =readFileSheet("Ventas")
    
        return contenidoreportesventas

    
    def sheet_reportes_registro(self):
        contenidoreportesregistro =readFileSheet("Regristro_de_precio")
    
        return contenidoreportesregistro

    
    def sheet_reportes_ganancias(self):
        contenidoreportesganancias =readFileSheet("Ganancias")
    
        return contenidoreportesganancias

    
    def sheet_reportes_gastos(self):
        contenidoreportesgastos =readFileSheet("Gastos")
    
        return contenidoreportesgastos

  
    def sheet_reportes_turnos(self):
        contenidoreportesturnos =readFileSheet("Turnos")
    
        return contenidoreportesturnos
      