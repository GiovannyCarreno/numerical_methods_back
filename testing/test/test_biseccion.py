import unittest
import pytest
import sympy as sp

from LogicMetodos.Biseccion import convertir_ecuacion, biseccion_solver

class TestFunciones(unittest.TestCase):
    def test_convertir_ecuacion(self):
        # Prueba convertir_ecuacion con una ecuación válida
        ecuacion = "2*x^2 - 4"
        funcion, x = convertir_ecuacion(ecuacion)
        self.assertTrue(callable(funcion))
        self.assertEqual(x, sp.symbols('x'))

@pytest.mark.parametrize(
    'funcion, a, b, expected',
    [
        ('sqrt(x) - 2', 0, 5, 4),
        ('x**2 - 4', 1, 3, 2),
        ('x**3 - 2*x - 5', 2, 3, 2.0945),
        ('x**3 + x**2 - x - 1', 0, 2, 1)
    ]
)
def test_biseccion_solver(funcion, a, b, expected):
    ecuacion, x = convertir_ecuacion(funcion)
    raiz, errores = biseccion_solver(ecuacion, a, b)
    assert raiz == pytest.approx(expected, rel=1e-4)

    


