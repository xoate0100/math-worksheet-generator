import unittest
from src.subtraction_worksheet import SubtractionWorksheet

class TestSubtractionWorksheet(unittest.TestCase):
    """Unit tests for the SubtractionWorksheet class."""
    
    def test_generate_problems_count(self):
        """Test that the correct number of subtraction problems are generated."""
        worksheet = SubtractionWorksheet(num_problems=5)
        problems = worksheet.generate_problems()
        self.assertEqual(len(problems), 5)
    
    def test_problem_format(self):
        """Test that each generated problem is in the correct format."""
        worksheet = SubtractionWorksheet(num_problems=3)
        problems = worksheet.generate_problems()
        for problem in problems:
            self.assertRegex(problem, r"\d+ - \d+ = ")

    def test_random_number_range(self):
        """Test that generated numbers fall within the expected range and the first number is always greater than or equal to the second."""
        worksheet = SubtractionWorksheet(num_problems=10)
        problems = worksheet.generate_problems()
        for problem in problems:
            a, b = map(int, problem.split('-'))
            self.assertGreaterEqual(a, 10)
            self.assertLessEqual(a, 100)
            self.assertGreaterEqual(b, 0)
            self.assertLessEqual(b, a)

    def test_display_problems(self):
        """Test that the dis