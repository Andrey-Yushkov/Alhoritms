import unittest
from lab4.task11.src.task11 import process_queue

class TestTask11(unittest.TestCase):
    def test_task11(self):
        n1, m1, demands1 = 3, 2, [1, 2, 3]
        n2, m2, demands2 = 4, 5, [2, 5, 2, 3]

        result1 = process_queue(n1, m1, demands1)
        result2 = process_queue(n2, m2, demands2)

        self.assertEqual(result1, ["2", "3 1"])
        self.assertEqual(result2, ["3", "4 1 2"])

    def test_no_people_left(self):
        n, m, demands = 2, 10, [1, 1]

        result = process_queue(n, m, demands)

        self.assertEqual(result, ["-1"])

    def test_partial_completion(self):
        n, m, demands = 4, 3, [1, 1, 1, 1]

        result = process_queue(n, m, demands)

        self.assertEqual(result, ["1", "1"])

    def test_large_demand(self):
        n, m, demands = 5, 5, [5, 5, 5, 5, 5]

        result = process_queue(n, m, demands)

        self.assertEqual(result, ["5", "4 4 4 4 4"])

    def test_edge_case_no_demands(self):
        n, m, demands = 3, 10, [0, 0, 0]

        result = process_queue(n, m, demands)

        self.assertEqual(result, ["-1"])

    def test_one_person(self):
        n, m, demands = 1, 1, [10]

        result = process_queue(n, m, demands)

        self.assertEqual(result, ["1", "9"])


if __name__ == '__main__':
    unittest.main()