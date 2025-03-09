import unittest
from lab6.utils import *
from lab6.task2.src.task2 import main, phone_book


class TestTask2(unittest.TestCase):

    def test_should_add_and_find_number(self):
        data = [
            ["add", "911", "police"],
            ["find", "911"]
        ]
        expected_result = ["police"]

        result = phone_book(data)

        self.assertEqual(result, expected_result)

    def test_should_delete_and_find_number(self):
        data = [
            ["add", "1234567890", "John Doe"],
            ["del", "1234567890"],
            ["find", "1234567890"]
        ]
        expected_result = ["not found"]

        result = phone_book(data)

        self.assertEqual(result, expected_result)

    def test_should_handle_multiple_commands(self):
        data = [
            ["add", "911", "police"],
            ["add", "112", "ambulance"],
            ["find", "911"],
            ["find", "112"],
            ["del", "112"],
            ["find", "112"]
        ]
        expected_result = ["police", "ambulance", "not found"]

        result = phone_book(data)

        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        expected_time = 6

        time = time_data(main)

        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        expected_memory = 512

        current, peak = memory_data(main)

        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == "__main__":
    unittest.main()
