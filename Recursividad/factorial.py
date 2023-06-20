#es una multiplicacion sucesiva descendiente hasta 1 de un numero

#factorial = !5 => 5x4x3x2x1 => 120
#factorial = !7 => 7x6x5x4x3x2x1 => 5040
#factorial = !4 => 4x3x2x1 => 24

def factorial(numero):
    if numero > 1:
        return numero * factorial(numero-1)
    return 1

# operador ternario: return 1 if numero <=1 else numero * factorial(numero-1)

print(factorial(5))

#factorial(5) => 5 * factorial(4)
#factorial(4) => 4 * factorial(3)
#factorial(3) => 3 * factorial(2)
#factorial(2) => 2 * 1
#factorial(1) => 1