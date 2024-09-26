import random

class AdditionWorksheet:
    """Class to generate addition worksheets based on speed arithmetic techniques."""
    
    def __init__(self, num_problems: int = 10):
        """
        Initializes the AdditionWorksheet.

        Args:
            num_problems (int): The number of addition problems to generate.
        """
        self.num_problems = num_problems

    def generate_problems(self):
        """
        Generate a list of addition problems using horizontal addition techniques.
        
        Returns:
            list: A list of formatted addition problems as strings.
        """
        problems = []
        for _ in range(self.num_problems):
            a, b = self._generate_numbers()
            problems.append(f"{a} + {b} = ")
        return problems

    def _generate_numbers(self):
        """
        Generates two random numbers for an addition problem.

        Returns:
            tuple: A tuple containing two integers.
        """
        return random.randint(0, 100), random.randint(0, 100)

    def display_problems(self):
        """
        Display the generated addition problems in a readable format.
        """
        problems = self.generate_problems()
        for problem in problems:
            print(problem)
