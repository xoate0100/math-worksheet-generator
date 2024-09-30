import random

class SubtractionWorksheet:
    """Class to generate subtraction worksheets based on speed arithmetic techniques."""
    
    def __init__(self, num_problems: int = 10):
        """
        Initializes the SubtractionWorksheet.

        Args:
            num_problems (int): The number of subtraction problems to generate.
        """
        self.num_problems = num_problems

    def generate_problems(self):
        """
        Generate a list of subtraction problems using horizontal subtraction techniques.
        
        Returns:
            list: A list of formatted subtraction problems as strings.
        """
        problems = []
        for _ in range(self.num_problems):
            a, b = self._generate_numbers()
            problems.append(f"{a} - {b} = ")
        return problems

    def _generate_numbers(self):
        """
        Generates two random numbers for a subtraction problem.

        Returns:
            tuple: A tuple containing two integers, ensuring the first is greater than or equal to the second.
        """
        a = random.randint(10, 100)
        b = random.randint(0, a)
        return a, b

    def display_problems(self):
        """
        Display the generated subtraction problems in a readable format.
        """
        problems = self.generate_problems()
        for problem in problems:
            print(problem)