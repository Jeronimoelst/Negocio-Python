from django import template
from math import isnan


# Create your tests here.
register=template.Library()

@register.filter(name="split")

def split(value, key):

    return value.split(key)


@register.filter(name="checkmonto")

def checkmonto(value):
    nuevovalor=""
    if value == '':
        nuevovalor='No'
    else:
        nuevovalor="$"+str(value)
    return nuevovalor    


@register.filter(name="checkconcepto")

def checkconcepto(value):
    nuevovalor=""
    if type(value) == float:
        nuevovalor='No'
    else:
        nuevovalor = value
    return nuevovalor    

@register.filter(name="checkpedido")

def checkpedido(value):
    nuevovalor=""
    if type(value) == float:
        nuevovalor='No'
    else:
        nuevovalor="$"+str(value)
    return nuevovalor    

@register.filter(name="checknombre")

def checknombre(value):
    nuevovalor=""
    if type(value) == float:
        nuevovalor='No'
    else:
        nuevovalor=str(value)
    return nuevovalor    



@register.filter(name="checkventa")

def checkventa(value):
    nuevovalor=""
    if isnan(int(value)):
        nuevovalor='No'
    else:
        nuevovalor="$"+str(value)
    return nuevovalor   

@register.filter(name="checkctelefono")

def checkctelefono(value):
    nuevovalor=""
    if type(value) == float:
        nuevovalor='No'
    else:
        nuevovalor = value
    return nuevovalor  

@register.filter(name="checkganancia")

def checkganancia(value):
    nuevovalor=""
    if type(value) == float:
        nuevovalor='No'
    else:
        nuevovalor="%"+str(value)
    return nuevovalor   

@register.filter(name="checkcompra")

def checkcompra(value):
    nuevovalor=""
    if isnan(value):
        nuevovalor='No'
    else:
        nuevovalor="$"+str(value)
    return nuevovalor  


@register.filter(name="checkunidades")

def checkunidades(value):
    nuevovalor=""
    if type(value) == float:
        nuevovalor='No'
    else:
        nuevovalor=str(value)
    return nuevovalor  

