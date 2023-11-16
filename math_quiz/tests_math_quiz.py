import unittest
from math_quiz import get_number, select_operator, do_math


class TestMathGame(unittest.TestCase):

    def test_get_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operator_selection(self):
        #  Test if random operator is selected from the options
        allowed_operators = ("+", "-", "*")
        for _ in range(1000):
             rand_operator = select_operator()
             self.assertTrue(rand_operator in allowed_operators)

    def test_math(self):
        # Test the below test cases for math operation
            test_cases = [
                (5, 2, '+', '5 + 2', 7),\
                (4, 6, '*', '4 * 6', 24),\
                (10, 8, '-', '10 - 8', 2)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                equation, ans = do_math(num1, num2, operator)
                self.assertTrue(equation == expected_problem and ans == expected_answer)


if __name__ == "__main__":
    unittest.main()
