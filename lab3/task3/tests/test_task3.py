import unittest

from lab3.task3.src.task3 import *


class TestTask3(unittest.TestCase):
    def test_example_a(self):
        (n, k), array = (3, 2), [2, 1, 3]
        expected = "NO"

        result, res_time, peak_memory = measure(sort_dolls, n, k, array)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_example_b(self):
        (n, k), array = (5, 3), [1, 5, 3, 4, 1]
        expected = "YES"

        result, res_time, peak_memory = measure(sort_dolls, n, k, array)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_example_c(self):
        (n, k), array = (7, 5), [1, 2, 4, 3, 5, 6, 7]
        expected = "NO"

        result, res_time, peak_memory = measure(sort_dolls, n, k, array)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")


if __name__ == '__main__':
    unittest.main()