import unittest
from lab5.task7.src.task7 import *
from lab5.utils import *


class TestTask7(unittest.TestCase):
    def test_sorted_array(self):
        array = [5, 3, 8, 4, 2]
        expected = [8, 5, 4, 3, 2]

        result, res_time, peak_memory = measure(heap_sort, array)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_large_array(self):
        array = [i for i in range(1000, 0, -1)]
        expected = sorted(array, reverse=True)

        result, res_time, peak_memory = measure(heap_sort, array)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_small_array(self):
        array = [3, 1, 2]
        expected = [3, 2, 1]

        result, res_time, peak_memory = measure(heap_sort, array)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")


if __name__ == "__main__":
    unittest.main()