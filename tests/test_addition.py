import unittest
from src.addition_worksheet import AdditionWorksheet

class TestAdditionWorksheet(unittest.TestCase):
    """Unit tests for the AdditionWorksheet class."""
    
    def test_generate_problems_count(self):
        """Test that the correct number of addition problems are generated."""
        worksheet = AdditionWorksheet(num_problems=5)
        problems = worksheet.generate_problems()
        self.assertEqual(len(problems), 5)
    
    def test_problem_format(self):
        """Test that each generated problem is in the correct format."""
        worksheet = AdditionWorksheet(num_problems=3)
        problems = worksheet.generate_problems()
        for problem in problems:
            self.assertRegex(problem, r"\d+ \+ \d+ = ")

    def test_random_number_range(self):
        """Test that generated numbers fall within the expected range."""
        worksheet = AdditionWorksheet(num_problems=10)
        problems = worksheet.generate_problems()
        for problem in problems:
            # Extract numbers from the problem string by removing spaces
            a, b = map(int, problem.replace(" ", "").split('+'))
            self.assertGreaterEqual(a, 0)
            self.assertLessEqual(a, 100)
            self.assertGreaterEqual(b, 0)
            self.assertLessEqual(b, 100)

if __name__ == "__main__":
    unittest.main()
