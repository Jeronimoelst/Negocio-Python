import pandas as pd
from django.conf import settings

def readFileSheet(SheetName):
        file= pd.read_excel(settings.NEGOCIO_DB, sheet_name=SheetName, engine='openpyxl', converters={'ID':int}, na_values=[' ', '#N/A', '#N/AN/A', '#NA', '-1.#IND', '-1.#QNAN', '-NaN', '-nan', '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n /a', 'nan', 'nulo', None] ,na_filter= False ,keep_default_na =False)
        registros= pd.DataFrame(file)
        return registros
