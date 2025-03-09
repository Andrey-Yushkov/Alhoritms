import unittest
from lab4.task5.src.task5 import Stack

class TestTask5(unittest.TestCase):
    def test_task5(self):
        stack = Stack()

        stack.push(2)
        stack.push(1)
        max1 = stack.max()
        stack.pop()
        max2 = stack.max()
        stack.push(7)
        max3 = stack.max()

        self.assertEqual(max1, 2)
        self.assertEqual(max2, 2)
        self.assertEqual(max3, 7)

    def test_empty_stack(self):
        stack = Stack()

        max_value = stack.max()

        self.assertIsNone(max_value)


if __name__ == '__main__':
    unittest.main()