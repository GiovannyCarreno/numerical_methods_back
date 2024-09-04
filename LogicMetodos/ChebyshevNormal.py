import numpy as np
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

def simplificar_ecuacion(ecuacion):
    x = sp.symbols('x')

    if 'x' not in ecuacion:
        raise ValueError('La ecuación debe estar en terminos de x.')
    
    try:
        expresion = sp.sympify(ecuacion, locals={'e': sp.E})
        expresion_simplificada = sp.sympify(expresion)

        return expresion_simplificada
    except sp.SympifyError:
        raise ValueError('La ecuacion aproximada no es valida.')
    
def aproximar_funcion(ecuacion, n):
    if n < 1:
        raise ValueError('El grado del polinomio de Chebyshev no puede ser menor que 1.')

    funcion = convertir_ecuacion(ecuacion)
    i = 0
    k = 0
    ak = []
    funcion_aproximada = ''
    while i < n:
        j = 0
        sak = 0
        while j < n:
            xn = np.cos((np.pi*(2*j+1))/(2*n))
            fxn = funcion(xn)
            sak += fxn*(np.cos(i*np.arccos(xn)))
            j += 1
        ak.append((2/n)*sak)
        i += 1
    
    while k < n:
        if k == 0:
            funcion_aproximada += f'{ak[k]/2:.10f} + '
        elif k != n-1:
            funcion_aproximada += f'{ak[k]:.10f}*(cos({k}*acos(x))) + '
        else:
            funcion_aproximada += f'{ak[k]:.10f}*(cos({k}*acos(x)))'
        k += 1
    
    return cambiar_notacion(simplificar_ecuacion(funcion_aproximada)), funcion_aproximada

def cambiar_notacion(cadena):
    if 'e' not in str(cadena):
        return cadena
    else:
        arreglo = str(cadena).split('e')
        cadena_final = ''
        i = 0
        while i < len(arreglo):
            if i != len(arreglo)-1:
                cadena_final += f'{arreglo[i]}*10^'
            else:
                cadena_final += f'{arreglo[i]}'
            i += 1
        return cadena_final