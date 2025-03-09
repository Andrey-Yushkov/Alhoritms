import unittest
from lab3.task1.src.task1 import *


def answer(testlist):
    return sorted(testlist)


class TestTask1(unittest.TestCase):
    def test_should_sort_empty(self):
        testlist = []

        result, res_time, peak_memory = measure(random_quick_sort, testlist)

        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_should_sort_basic(self):
        testlist = [2, 3, 9, 2, 2]

        result, res_time, peak_memory = measure(random_quick_sort, testlist)

        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_should_sort_random(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(10000)]

        result, res_time, peak_memory = measure(random_quick_sort, testlist)

        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_should_sort_few_different(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20)] * 500

        result, res_time, peak_memory = measure(random_quick_sort3, testlist)

        self.assertEqual(result, answer(testlist))
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_should_compare_properly(self):
        testlist = [random.randint(-10 ** 9, 10 ** 9) for _ in range(20)] * 500

        result, end_time, peak_memory = measure(random_quick_sort, testlist)
        result3, end_time3, peak_memory = measure(random_quick_sort3, testlist)

        self.assertGreater(end_time, end_time3)


if __name__ == '__main__':
    unittest.main()