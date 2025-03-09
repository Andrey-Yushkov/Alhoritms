import unittest
from lab4.task4.src.task4 import check_brackets

class TestTask4(unittest.TestCase):
    def test_task4(self):
        cases = [
            ("[]", "Success"),
            ("{}", "Success"),
            ("()", "Success"),
            ("{[()]}", "Success"),
            ("foo(bar);", "Success"),
            ("", "Success")
        ]

        for sequence, expected in cases:
            result = check_brackets(sequence)

            self.assertEqual(result, expected)

    def test_error_cases(self):
        cases = [
            ("{", 1),
            ("}", 1),
            ("{[}", 3),
            ("foo(bar[i);", 10),
            ("(}", 2)
        ]

        for sequence, expected in cases:
            result = check_brackets(sequence)

            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()