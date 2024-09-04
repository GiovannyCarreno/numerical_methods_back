import sympy as sp
import numpy as np

def convertir_ecuacion(ecuacion):
    x, y = sp.symbols('x y')
    if 'x' not in ecuacion and 'y' not in ecuacion:
        raise ValueError('La ecuacion debe estar en terminos de x y/o y.')
    try:
        expresion = sp.sympify(ecuacion, locals={'e': sp.E, 'I': sp.I})
        expresion_simplificada = sp.sympify(expresion)
        return sp.lambdify([x, y], expresion_simplificada, modules=['numpy', {'sqrt': np.sqrt}]), x, y
    except sp.SympifyError:
        raise ValueError('La ecuación ingresada no es valida.')

def metodo_euler(ecuacion, a, b, y0, n):
    f, x, y = convertir_ecuacion(ecuacion)
    h = (b - a) / n  # Tamaño del paso
    x_vals = np.linspace(a, b, n + 1)
    y_vals = np.zeros(n + 1)
    y_vals[0] = y0
    for i in range(1, n + 1):
        y_vals[i] = y_vals[i - 1] + h * f(x_vals[i - 1], y_vals[i - 1])
    return x_vals.tolist(), y_vals.tolist()

# Ejemplo con la función dada
##ecuacion = "(0.1*(y)**(1/2))+(0.4*x**2)"
##a, b = 2, 2.5
##y0 = 4
##n = 10

##x_vals, y_vals = metodo_euler(ecuacion, a, b, y0, n)
##print("Resultado para y' = (0.1*(y)**(1/2))+(0.4*x**2):")
##print("x:", x_vals)
##print("y:", y_vals)