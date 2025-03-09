import unittest
import random
from lab7.task4.src.task4 import sample_main


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_basic_case(self):
        input_data = ([2, 7, 5], [2, 5])
        expected_output = 2

        result = sample_main(*input_data)

        self.assertEqual(result, expected_output)

    def test_full_match(self):
        input_data = ([1, 2, 3, 4], [1, 2, 3, 4])
        expected_output = 4

        result = sample_main(*input_data)

        self.assertEqual(result, expected_output)

    def test_large_input(self):
        input_data = (
            [random.randint(1, 100) for _ in range(100)],
            [random.randint(1, 100) for _ in range(100)],
        )

        result = sample_main(*input_data)

        self.assertTrue(isinstance(result, int))

    def test_no_common_subsequence(self):
        input_data = ([7], [1])
        expected_output = 0

        result = sample_main(*input_data)

        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()