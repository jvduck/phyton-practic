#una potencia es un numero multiplicado por si mismo una determinada cant de veces
""" 
ej 3**4 => 3x3x3x3 
5**3 => 5x5x5
"""

# def potencia(base,exponente):
#     if exponente > 1:
#         return base * potencia(base,exponente-1)
#     return base
    
def potencia(base,exponente):
    if exponente < 0:
        return("No ingrese numeros negativos")
    if exponente == 0: 
        return 1
    if exponente == 1:
        return base
    return base * potencia(base,exponente-1)
    
"""
def multiplicar(base,multiplicador):
    if multiplicador > 1:
        return base + multiplicar(base,multiplicador-1)
    return base
"""
print(potencia(5,3))