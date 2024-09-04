import pytest
import sympy as sp
from LogicMetodos.Biseccion import convertir_ecuacion, calcular_error_porcentual, biseccion_solver

@pytest.mark.parametrize(
    "ecuacion, intervalo, expected_root, tol",
    [
        ('x**3 - x - 2', (1, 2), 1.521, 1e-3),
        ('x**2 - 4', (1, 3), 2, 1e-3),
        ('x**2 - 4', (-3, -1), -2, 1e-3)
    ]
)
def test_biseccion_solver(ecuacion, intervalo, expected_root, tol):
    func, x = convertir_ecuacion(ecuacion)
    a, b = intervalo
    root, errores = biseccion_solver(func, a, b, tol=tol)
    assert abs(root - expected_root) < tol


