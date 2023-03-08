
class Helpers:

    def setear_id(self, writer, pagina, id):
       return writer.sheets[pagina].max_row if id==str() else id 
    
    def setear_fecha(self, fecha):
        fechaparseada = fecha.replace("-", "/")
        a = fechaparseada.split("/")
        nuevafecha = a[1]+'/'+a[2]+'/'+a[0]
        return nuevafecha

    