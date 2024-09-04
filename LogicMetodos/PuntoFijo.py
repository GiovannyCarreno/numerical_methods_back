import sympy as sp
import numpy as np

def convertir_ecuacion(ecuacion):
    x = sp.symbols('x')
    if 'x' not in ecuacion:
        raise ValueError("La ecuación debe estar en términos de 'x'.")
    try:
        expresion = sp.sympify(ecuacion, locals={'e': sp.E})
        expresion_simplificada = sp.simplify(expresion)
        return expresion_simplificada, x
    except sp.SympifyError:
        raise ValueError("La ecuación ingresada no es válida.")

def calcular_error_porcentual(valor_actual, valor_anterior):
    if abs(valor_anterior) < 1e-10:
        return 10000
    else:
        return abs((valor_actual - valor_anterior) / valor_anterior) * 100

def complex_to_dict(c):
    return {'real': float(c.real), 'imag': float(c.imag)}

def punto_fijo(ecuacion, x, valor_inicial, max_iter=100, tolerancia=1e-4):
    iteraciones = []
    aproximaciones = [complex(valor_inicial)]
    errores = []
    x_actual = complex(valor_inicial)

    for i in range(1, max_iter + 1):
        x_anterior = x_actual
        x_actual = complex(ecuacion.subs(x, x_anterior).evalf())
        error_actual = calcular_error_porcentual(x_actual, x_anterior)
        
        iteraciones.append(i)
        aproximaciones.append(x_actual)
        errores.append((i, float(error_actual)))

        if error_actual < tolerancia:
            return complex_to_dict(x_actual), errores

    return None, errores

def punto_fijo_inicio(imputecuacion, valor_inicial):
    ecuacion, x = convertir_ecuacion(imputecuacion)
    despejes = sp.solve(ecuacion, x)
    raices = []
    for despeje in despejes:
        raiz, errores = punto_fijo(despeje, x, valor_inicial)
        if raiz is not None:
            raices.append(raiz)
    return raices, errores

# Ejemplo de ecuación: x = -(2*x^3 + 4)
##ecuacion = '-(2*x**3 + 4)'

# Llamar al método de punto fijo
##raices, errores = punto_fijo_inicio(ecuacion, 1)

# Mostrar resultados
##print("Raíces encontradas:")
##for raiz in raices:
##    print(f"{raiz.real:.6f} + {raiz.imag:.6f}i")

##print("\nErrores por iteración:")
##for iteracion, error in errores:
  ##  print(f"Iteración {iteracion}: Error porcentual = {error:.6f}%")