import unittest
from lab4.task1.src.task1 import process_stack_commands
from lab4.utils import measure


class TestTask1(unittest.TestCase):

    def test_stack_operations(self):
        commands = [
            "+ 10",
            "+ 20",
            "+ 30",
            "-",
            "-",
            "-",
        ]
        expected = [30, 20, 10]

        result, res_time, peak_memory = measure(process_stack_commands, commands)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_empty_stack(self):
        commands = ["-"]
        expected = [None]

        result, res_time, peak_memory = measure(process_stack_commands, commands)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")

    def test_mixed_operations(self):
        commands = [
            "+ 5",
            "+ 15",
            "-",
            "+ 25",
            "-",
            "-",
        ]
        expected = [15, 25, 5]

        result, res_time, peak_memory = measure(process_stack_commands, commands)

        self.assertEqual(result, expected)
        self.assertLessEqual(res_time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(peak_memory, 256, "Memory usage exceeded 256 MB")


if __name__ == '__main__':
    unittest.main()