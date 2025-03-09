import unittest

from lab3.task6.src.task6 import *


class TestTask6(unittest.TestCase):
    def test_should_int_sort_example_a(self):
        (n, m), array_a, array_b = (4, 4), [7, 1, 4, 9], [2, 7, 8, 11]
        expected = 51

        combinations = multiply(n, m, array_a, array_b)
        result, res_time, peak_memory = measure(sum_tenth, combinations)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 512, "Memory usage exceeded 512 MB")

    def test_should_int_sort_example_b(self):
        (n, m), array_a, array_b = (2, 2), [1, 2], [3, 4]
        expected = 3

        combinations = multiply(n, m, array_a, array_b)
        result, res_time, peak_memory = measure(sum_tenth, combinations)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 512, "Memory usage exceeded 512 MB")

    def test_should_int_sort_example_c(self):
        (n, m), array_a, array_b = (1, 1), [0], [99]
        expected = 0

        combinations = multiply(n, m, array_a, array_b)
        result, res_time, peak_memory = measure(sum_tenth, combinations)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 512, "Memory usage exceeded 512 MB")


if __name__ == '__main__':
    unittest.main()