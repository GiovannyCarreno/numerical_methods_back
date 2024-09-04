import pytest
from LogicMetodos.NewtonRaphson import newton_raphson

@pytest.mark.parametrize(
    'ecuacion, variable, x0, expected',
    [
        ('4*x**2 + x - 4', 'x', 200, 0.8827),
        ('sqrt(x) - 2', 'x', 10, 4),
        ('x**2 - 4', 'x', 3, 2),
        ('x**3 - 2*x - 5', 'x', 2, 2.0945),
        ('x**3 + x**2 - x - 1', 'x', 2, 1)
    ]
)
def test_newton_raphson(ecuacion, variable, x0, expected):
    raiz, errores = newton_raphson(ecuacion, variable, x0)
    assert raiz == pytest.approx(expected, rel=1e-4)