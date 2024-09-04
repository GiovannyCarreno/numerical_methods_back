import sympy as sp

def convertir_ecuacion (ecuacion):
    #Se define el simbolo de la bariable
    x = sp.symbols('x')

    #Verifica si la variable está en la ecuación
    if 'x' not in ecuacion:
        raise ValueError('La ecuacion debe estar en terminos de x.')
    
    try:
        #Convierte la cadena de ecuación a una expreción simbólica
        expresion = sp.sympify(ecuacion, locals={'e': sp.E})

        #Simplifica la expresión
        expresion_simplificada = sp.sympify(expresion)

        #Devuelve la funcion evaluable y el simbolo x
        return sp.lambdify(x, expresion_simplificada, modules='numpy'), x
    except sp.SympifyError:
        raise ValueError('La ecuación ingresada no es valida.')

def trapeze_solver(equation, a, b, n):
    if n < 1 :
        raise ValueError('El número de intervalos no puede ser menor que 1')
    #Si los limites de los intervalos son iguales, el area bajo la curva siempre es cero
    if a == b:
        return 0

    if a < b:
        if n > 1:
            #Define el ancho de los trapecios
            h = (b-a)/n
            intervalos = a
            area = 0
            #Aplica el metodo de trapecio
            while intervalos <= b:
                if intervalos == a or intervalos == b:
                    area += equation(intervalos)
                    intervalos += h
                else:
                    area += 2*(equation(intervalos))
                    intervalos += h
        
            return (h/2)*area
    
        if n == 1:
            area = (b-a)*((equation(a)+equation(b))/2)

            return area
    #Aplica el método de Trapecio en caso de que los intervalos esten invertidos
    if a > b:
        if n > 1:
            #Define el ancho de los trapecios
            h = (a-b)/n
            intervalos = b
            area = 0
            #Aplica el método de trapecio
            while intervalos <= a:
                if intervalos == a or intervalos == b:
                    area += equation(intervalos)
                    intervalos += h
                else:
                    area += 2*(equation(intervalos))
                    intervalos += h
        
            return (h/2)*area
    
        if n == 1:
            area = (a-b)*((equation(a)+equation(b))/2)

            return area

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
        return 0, 0
    
    error = abs((integral_real - integral_aprox) / integral_aprox) * 100
    return integral_real, error