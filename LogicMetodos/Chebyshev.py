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
    if 'x' not in ecuacion:
        raise ValueError('La ecuación aproximada no está en terminos de x.')
    
    try:
        expresion = sp.sympify(ecuacion, locals={'e': sp.E})
        expresion_simplificada = sp.sympify(expresion)

        return expresion_simplificada
    except sp.SympifyError:
        raise ValueError('La ecuacion aproximada no es valida.')
    
def aproximar_ecuacion(ecuacion, a, b, n):
    if n < 1:
        raise ValueError('El grado del polinomio de Chebyshev no puede ser menor que 1.')

    funcion = convertir_ecuacion(ecuacion)
    cn = []
    i = 0
    k = 0

    while i <= n:
        j = 0
        scn = 0
        while (j <= n):
            tk = np.cos((np.pi*(j+0.5))/(n+1))
            gtk = funcion(cambio_de_variable(a,b,tk))
            scn += gtk*np.cos((i*np.pi*(j+0.5))/(n+1))
            j += 1
        cn.append((2/(n+1))*scn)
        i += 1

    funcion_aproximada = ''

    while k <= n:
        if k == 0:
            funcion_aproximada += f'{cn[k]/2:.10f} + '
        elif k != n:
            funcion_aproximada += f'{cn[k]:.10f}*cos({k}*(acos((2*x-({a+b}))/{b-a}))) + '
        else:
            funcion_aproximada += f'{cn[k]:.10f}*cos({k}*(acos((2*x-({a+b}))/{b-a})))'
        k += 1

    return cambiar_notacion(simplificar_ecuacion(funcion_aproximada))

def cambio_de_variable(a,b,t):
    return (((b-a)/2)*t)+((a+b)/2)

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

