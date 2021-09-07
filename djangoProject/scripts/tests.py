import traversal as Lab
import unittest
import numpy as np
import random
# возвращающает 1 с вероятностью chance
def random_bool(chance):
    try:
        if random.random() <= chance:
            return 1
        else:
            return 0
    except TypeError:
        print("Error: Function random_bool received invalid argument/n")
        return 1


# создает двумерную матрицу размера size с степенью связанности узлов chance
def create_matrix(size, chance):
    try:
        N = np.zeros((size, size), dtype=int)
    except ValueError:
        print("Error: function create_matrix received negative matrix size/n")
        size = 10
        N = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            N[i][j] = random_bool(chance)
        N[i][i] = False
    N = np.maximum(N, N.transpose())
    return N



# корректный путь между вершинами 0 и 9 для тестовой матрицы
true_path = [0, 1, 3, 4, 9]

# матрица смежности с существующим путем между вершинами 0 и 9
test_matr = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
]

not_bool_matr = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 2, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, "z", 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, "ads", 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
]

rectangular_matr=[
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1]
]


class RouteSearcher(unittest.TestCase):

    # def setUp(self):
    #     self.form= interface.ExampleApp()



# Черный ящик
    # Поиск маршрута между заведомо несвязанными вершинами.
    # на входе нулевая матрица
    def test_InvalidWay(self):
        self.assertEqual(Lab.traversal_wrapper(create_matrix(10, 0), 0, 9), False)

    # Поиск пути в матрице смежности. Путь существует
    def test_ValidRoute(self):
        self.assertEqual(Lab.traversal_wrapper(test_matr, 0, 9), true_path)

    # Поиск пути между элементами, которые не существуют в матрице смежности
    def test_ValuesOutOfBorders(self):
        self.assertEqual(Lab.traversal_wrapper(test_matr, -1, 10), False)

# Белый ящик
    # Поиск пути в неквадратной матрице
    def test_RectangularMatrix(self):
        with self.assertRaises(Lab.DimensionException):
            Lab.traversal_wrapper(rectangular_matr, 0, 1)

    # Поиск пути в матрице, содержащей значения кроме 0 и 1
    def test_NotBoolMatrix(self):
        with self.assertRaises(ValueError):
            Lab.traversal_wrapper(not_bool_matr, 0, 9)


if __name__ == '__main__':
    unittest.main()