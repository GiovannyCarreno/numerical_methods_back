import pytest
import sympy as sp
from LogicMetodos.Secante import secante, convertir_ecuacion

@pytest.mark.parametrize(
    'funcion, x0, x1, expected',
    [
        ('4*x**2 + x - 4', 200, 100, 0.8827),
        ('sqrt(x) - 2', 10, 6, 4),
        ('x**2 - 4', 3, 2.5, 2),
        ('x**3 - 2*x - 5', 2, 1, 2.0945),
        ('x**3 + x**2 - x - 1', 2, 1.5, 1)
    ]
)
def test_secante(funcion, x0, x1, expected):
    func, x = convertir_ecuacion(funcion)
    root, errores = secante(func, x0, x1)
    assert root == pytest.approx(expected, rel=1e-4)