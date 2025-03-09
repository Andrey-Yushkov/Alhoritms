import unittest
from lab5.task2.src.task2 import *
from lab5.utils import *



class TestTask2(unittest.TestCase):
    def test_simple_tree(self):
        n = 5
        parents = [-1, 0, 0, 1, 1]
        expected = 3

        result, res_time, peak_memory = measure(calculate_height, n, parents)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_single_node(self):
        n = 1
        parents = [-1]
        expected = 1

        result, res_time, peak_memory = measure(calculate_height, n, parents)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_linear_tree(self):
        n = 4
        parents = [-1, 0, 1, 2]
        expected = 4

        result, res_time, peak_memory = measure(calculate_height, n, parents)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_balanced_tree(self):
        n = 7
        parents = [-1, 0, 0, 1, 1, 2, 2]
        expected = 3

        result, res_time, peak_memory = measure(calculate_height, n, parents)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

if __name__ == "__main__":
    unittest.main()