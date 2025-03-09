import unittest
from lab7.task2.src.task2 import optimal_sequence
from lab7.utils import measure

class TestTask2(unittest.TestCase):

    def test_example_case_1(self):
        n = 1

        result, res_time, peak_memory = measure(optimal_sequence, n)

        self.assertEqual(result, (0, [1]))
        self.assertLessEqual(res_time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_example_case_2(self):
        n = 5

        result, res_time, peak_memory = measure(optimal_sequence, n)

        self.assertEqual(result, (3, [1, 2, 4, 5]))
        self.assertLessEqual(res_time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_large_input(self):
        n = 96234

        result, res_time, peak_memory = measure(optimal_sequence, n)

        self.assertGreater(len(result[1]), 0, "Sequence should not be empty")
        self.assertLessEqual(res_time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

if __name__ == '__main__':
    unittest.main()