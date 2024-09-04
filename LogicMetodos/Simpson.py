import sympy as sp

def convertir_ecuacion(ecuacion):
    x = sp.symbols('x')

    if 'x' not in ecuacion:
        raise ValueError('La ecuación debe estar en terminos de x.')
    
    try:
        expresion = sp.sympify(ecuacion, locals={'e': sp.E})
        expresion_simplificada = sp.sympify(expresion)

        return sp.lambdify(x, expresion_simplificada, modules = 'numpy')
    except sp.SympifyError:
        raise ValueError('La ecuacion ingresada no es valida.')
    
def simpson_solver(equation, a, b, n):
    if n < 2 :
        raise ValueError('El número de intervalos no puede ser menor que 2 y debe ser par')
    #Si los limites de los intervalos son iguales, el area bajo la curva siempre es cero
    if a == b:
        return 0
    
    if n == 2:
        return ((b-a)/6)*(equation(a)+4*equation((a+b)/2)+equation(b))
    #Aplica el método de Simpson
    if n > 2 and n%2 == 0 and a < b:
        h = (b-a)/n
        intervalo = a
        sumatoria_xni = 0
        sumatoria_xi = 0

        while intervalo < b:
            sumatoria_xni += (equation(intervalo)+(equation(intervalo+h)))/2
            intervalo += h
        
        intervalo = a

        while intervalo <= b:
            if intervalo != a and intervalo != b:
                sumatoria_xi += equation(intervalo)
            intervalo += h

        return ((b-a)/(6*n))*(equation(a)+(4*(sumatoria_xni))+(2*(sumatoria_xi))-equation(b))
    #Aplica el método de Simpson en caso de que los intervalos esten invertidos
    if n > 2 and n%2 == 0 and a > b:
        h = (a-b)/n
        intervalo = b
        sumatoria_xni = 0
        sumatoria_xi = 0

        while intervalo < a:
            sumatoria_xni += (equation(intervalo)+(equation(intervalo+h)))/2
            intervalo += h
        
        intervalo = b

        while intervalo <= a:
            if intervalo != b and intervalo != a:
                sumatoria_xi += equation(intervalo)
            intervalo += h

        return ((a-b)/(6*n))*(equation(b)+(4*(sumatoria_xni))+(2*(sumatoria_xi))-equation(a))
    else:
        raise ValueError('El numero de intervalos deve ser par')
    
# Definir la función para calcular el error
def calcular_error(func, a, b, integral_aprox):
    x = sp.Symbol('x')
    euler = sp.exp(1)
    f = sp.sympify(func).subs('e', euler)  # Sustituir 'e' por la constante de Euler
    
    if a < b:
        integral_real = sp.integrate(f, (x, a, b))
    elif a > b:
        integral_real = sp.integrate(f, (x, b, a))
    else:
        return 0
    
    error = abs((integral_real - integral_aprox) / integral_aprox) * 100
    return error