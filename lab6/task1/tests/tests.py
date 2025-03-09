import unittest
from lab6.utils import  *
from lab6.task1.src.task1 import main, operations


class TestOperations(unittest.TestCase):

    def test_should_add_and_query_element(self):
        data = [
            ('A', 1),
            ('?', 1),
            ('D', 1),
            ('?', 1)
        ]
        expected_result = ['Y', 'N']

        result = operations(data)

        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_elements(self):
        data = [
            ('A', 1),
            ('A', 2),
            ('A', 3),
            ('?', 1),
            ('?', 2),
            ('?', 3),
            ('D', 2),
            ('?', 2),
            ('?', 3)
        ]
        expected_result = ['Y', 'Y', 'Y', 'N', 'Y']

        result = operations(data)

        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        expected_time = 2

        time = time_data(main)

        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        expected_memory = 256

        current, peak = memory_data(main)


        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()