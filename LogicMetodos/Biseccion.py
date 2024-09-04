import sympy as sp

def convertir_ecuacion(ecuacion):
    # Define el símbolo de la variable
    x = sp.symbols('x')
    
    # Verifica si 'x' está en la ecuación
    if 'x' not in ecuacion:
        raise ValueError("La ecuación debe estar en términos de 'x'.")
    
    try:
        # Convierte la cadena de ecuación a una expresión simbólica
        expresion = sp.sympify(ecuacion, locals={'e': sp.E})
        
        # Simplifica la expresión
        expresion_simplificada = sp.simplify(expresion)
        
        # Devuelve una función evaluable y el símbolo 'x'
        return sp.lambdify(x, expresion_simplificada, modules='numpy'), x
    
    except sp.SympifyError:
        raise ValueError("La ecuación ingresada no es válida.")



def calcular_error_porcentual(valor_actual, valor_anterior):
    if valor_anterior == 0:
        return float('inf')
    else:
        return abs((valor_actual - valor_anterior) / valor_anterior) * 100

def biseccion_solver(equation_func, a, b, tol=1e-4, max_iterations=100):
    if equation_func(a) * equation_func(b) >= 0:
        raise ValueError("La función no cambia de signo en el intervalo [a, b].")

    iteration = 1
    previous_root = (a + b) / 2
    errores = []

    while (b - a) / 2 > tol and iteration < max_iterations:
        midpoint = (a + b) / 2
        if equation_func(midpoint) == 0:
            errores.append((iteration, 0))
            return midpoint, errores

        error_a = calcular_error_porcentual(midpoint, a)
        error_b = calcular_error_porcentual(midpoint, b)

        if error_a < tol:
            errores.append((iteration, error_a))
            return a, errores
        elif error_b < tol:
            errores.append((iteration, error_b))
            return b, errores

        if equation_func(a) * equation_func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

        iteration += 1
        error_actual = calcular_error_porcentual(midpoint, previous_root)
        errores.append((iteration, error_actual))
        previous_root = midpoint

    return (a + b) / 2, errores

