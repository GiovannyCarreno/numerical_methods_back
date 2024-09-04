import unittest
import numpy as np
from LogicMetodos.GaussSeidel import gauss_seidel

class TestGaussSeidel(unittest.TestCase):
    
    def setUp(self):
        self.A = np.array([[4, 1, 2],
                           [3, 5, 1],
                           [1, 1, 3]], dtype=float)
        self.b = np.array([4, 7, 3], dtype=float)
        self.x0 = np.zeros_like(self.b)
        self.tolerancia = 1e-6
        self.max_iter = 100
    
    def test_gauss_seidel_converge(self):
        resultado = gauss_seidel(self.A, self.b, self.x0, self.tolerancia, self.max_iter)
        self.assertIsNotNone(resultado)
        np.testing.assert_array_almost_equal(np.dot(self.A, resultado), self.b, decimal=5)
    
    def test_gauss_seidel_no_converge(self):
        A_no_dominante = np.array([[1, 2, 3],
                                   [4, 5, 6],
                                   [7, 8, 9]], dtype=float)
        with self.assertRaises(ValueError):
            gauss_seidel(A_no_dominante, self.b, self.x0, self.tolerancia, self.max_iter)
    
    def test_gauss_seidel_solucion_known(self):
        A_known = np.array([[10, -1, 2, 0],
                            [-1, 11, -1, 3],
                            [2, -1, 10, -1],
                            [0, 3, -1, 8]], dtype=float)
        b_known = np.array([6, 25, -11, 15], dtype=float)
        x0_known = np.zeros_like(b_known)
        resultado = gauss_seidel(A_known, b_known, x0_known, self.tolerancia, self.max_iter)
        solucion_esperada = np.array([1, 2, -1, 1], dtype=float)
        np.testing.assert_array_almost_equal(resultado, solucion_esperada, decimal=5)

if __name__ == '__main__':
    unittest.main()