from flask import Flask, request, jsonify
from LogicMetodos import NewtonRaphson, Biseccion, PuntoFijo, Secante, Jacobi, GaussSeidel, Simpson, Trapecio, Chebyshev, ChebyshevNormal, Euler 
import numpy as np
from flask import jsonify, request
import traceback
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/newtonRaphson', methods=['GET', 'POST'])
def newton_raphson_method():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        x0 = float(request.args.get('x0'))
        tol = float(request.args.get('tol'))

    elif request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        x0 = data['x0']
        tol = data['tol']

    try:
        equation_func, x = NewtonRaphson.convertir_ecuacion(funcion)
        raiz, errores = NewtonRaphson.newton_raphson(equation_func, str(x), x0, tol)
        return jsonify({
            'raiz': raiz,
            'errores': errores
        })
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/biseccion', methods=['GET', 'POST'])
def biseccion_method():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        tol = float(request.args.get('tol'))

    elif request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        a = data['a']
        b = data['b']
        tol = data['tol']

    try:
        equation_func, x = Biseccion.convertir_ecuacion(funcion)
        raiz, errores = Biseccion.biseccion_solver(equation_func, a, b, tol)
        return jsonify({
            'raiz': raiz,
            'errores': errores
        })
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/puntofijo', methods=['POST'])
def punto_fijo_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No se proporcionaron datos JSON'}), 400
        
        funcion = data.get('funcion')
        if not funcion:
            return jsonify({'error': 'No se proporcionó la función'}), 400
        
        valor_inicial = data.get('valor_inicial', 0)
        
        try:
            valor_inicial = float(valor_inicial)
        except ValueError:
            return jsonify({'error': 'El valor inicial debe ser un número'}), 400

        raices, errores = PuntoFijo.punto_fijo_inicio(funcion, valor_inicial)
        
        return jsonify({
            'raices': raices,
            'errores': errores
        })
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error en /puntofijo: {str(e)}")
        return jsonify({'error': f'Ocurrió un error interno: {str(e)}'}), 500

    
@app.route('/secante', methods=['GET', 'POST'])
def secante():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        x0 = float(request.args.get('x0'))
        x1 = float(request.args.get('x1'))
        tol = float(request.args.get('tol'))

    if request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        x0 = float(data['x0'])
        x1 = float(data['x1'])
        tol = float(data['tol'])

    try:  
        # Convertir la función a una expresión sympy
        equation_func, _ = Secante.convertir_ecuacion(funcion)
        
        # Calcular la raíz utilizando el método de la secante
        raiz, errores = Secante.secante(equation_func, x0, x1, tol)
        
        # Devolver el resultado como JSON
        return jsonify({
            'raiz': raiz,
            'errores': errores
            })
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/jacobi', methods=['GET', 'POST'])
def metodo_jacobi():
    if request.method == 'GET':
        A_str = request.args.get('A')
        b_str = request.args.get('b')
        x0_str = request.args.get('x0')
        tolerancia = float(request.args.get('tolerancia', 1e-6))
        max_iter = int(request.args.get('max_iter', 100))

    if request.method == 'POST':
        data = request.get_json()
        A_str = data['A']
        b_str = data['b']
        x0_str = data['x0']
        tolerancia = float(data['tolerancia'])
        max_iter = int(data['max_iter'])
        
    try:
        # Convertir los strings en arrays numpy bidimensionales
        A = np.array([list(map(float, row.split(','))) for row in A_str.split(';')])
        b = np.array(b_str.split(','), dtype=float)
        x0 = np.array(x0_str.split(','), dtype=float)
        
        # Llamar a la función de Jacobi
        resultado = Jacobi.jacobi(A, b, x0, tolerancia, max_iter)
        
        # Devolver el resultado como JSON
        return jsonify({'resultado': resultado.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/trapecio', methods=['GET', 'POST'])
def trapecio_metod():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        a = request.args.get('a')
        b = request.args.get('b')
        n = request.args.get('n')
    elif request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        a = data['a']
        b = data['b']
        n = data['n']
    try:
        equation, x = Trapecio.convertir_ecuacion(funcion)
        area = Trapecio.trapeze_solver(equation, float(a), float(b), int(n))
        integral_real, error = Trapecio.calcular_error(funcion, a, b, area)
        return jsonify({
            'Area:':float(area),
            'error': float(error)
            })
    except Exception as e:
        return jsonify({'Error': str(e)})

@app.route('/gauss-seidel', methods=['GET', 'POST'])
def metodo_gauss_seidel():
    if request.method == 'GET':
        A_str = request.args.get('A')
        b_str = request.args.get('b')
        x0_str = request.args.get('x0')
        tolerancia = float(request.args.get('tolerancia', 1e-6))
        max_iter = int(request.args.get('max_iter', 100))

    if request.method == 'POST':
        data = request.get_json()
        A_str = data['A']
        b_str = data['b']
        x0_str = data['x0']
        tolerancia = float(data['tolerancia'])
        max_iter = int(data['max_iter'])

    try:
        
        # Convertir los strings en arrays numpy bidimensionales
        A = np.array([list(map(float, row.split(','))) for row in A_str.split(';')])
        b = np.array(b_str.split(','), dtype=float)
        x0 = np.array(x0_str.split(','), dtype=float)
        
        # Llamar a la función de Gauss-Seidel
        resultado = GaussSeidel.gauss_seidel(A, b, x0, tolerancia, max_iter)
        
        # Devolver el resultado como JSON
        return jsonify({'resultado': resultado.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/simpson', methods=['GET', 'POST'])
def simpson_metod():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        a = request.args.get('a')
        b = request.args.get('b')
        n = request.args.get('n')
    elif request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        a = data['a']
        b = data['b']
        n = data['n']
    try:
        equation = Simpson.convertir_ecuacion(funcion)
        area = Simpson.simpson_solver(equation, float(a), float(b), int(n))
        error = Simpson.calcular_error(funcion, a, b, area)
        return jsonify({'Area:': float(area),
                        'Error': float(error)})
    except Exception as e:
        return jsonify({'Error': str(e)})

@app.route('/chebyshev2', methods=['GET', 'POST'])
def chebyshev2_method():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        n = request.args.get('n')
    elif request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        n = data['n']
    try:
        funcion_aproximada, funcion_aproximada_larga = ChebyshevNormal.aproximar_funcion(funcion, int(n))
        return jsonify({
            'funcion_aproximada': str(funcion_aproximada)
            })
    except Exception as e:
        return jsonify({'Error': str(e)})
    
@app.route('/chebyshev1', methods=['GET', 'POST'])
def chebyshev1_method():
    if request.method == 'GET':
        funcion = request.args.get('funcion')
        a = request.args.get('a')
        b = request.args.get('b')
        n = request.args.get('n')
    elif request.method == 'POST':
        data = request.get_json()
        funcion = data['funcion']
        a = data['a']
        b = data['b']
        n = data['n']
    try:
        funcion_aproximada = Chebyshev.aproximar_ecuacion(funcion, float(a), float(b), int(n))
        return jsonify({'funcion_aproximada': str(funcion_aproximada)})
    except Exception as e:
        return jsonify({'Error': str(e)})
    
@app.route('/euler', methods=['POST'])
def euler():
    data = request.get_json()
    ecuacion = data['ecuacion']
    a = float(data['a'])
    b = float(data['b'])
    y0 = float(data['y0'])
    n = int(data['n'])
    
    try:
        x_vals, y_vals = Euler.metodo_euler(ecuacion, a, b, y0, n)
        return jsonify({'x_vals': x_vals, 'y_vals': y_vals})
    except Exception as e:
        return jsonify({'error': str(e)}), 400    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)