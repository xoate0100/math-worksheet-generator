import random
import logging

class AdditionWorksheet:
    """Class to generate addition worksheets based on speed arithmetic techniques."""
    
    def __init__(self, num_problems: int = 10):
        """
        Initializes the AdditionWorksheet.

        Args:
            num_problems (int): The number of addition problems to generate.

        Raises:
            ValueError: If num_problems is less than 1.
        """
        self.logger = logging.getLogger(__name__)
        if num_problems < 1:
            error_msg = f"Number of problems must be at least 1, got {num_problems}"
            self.logger.error(error_msg)
            raise ValueError(error_msg)
        self.num_problems = num_problems
        self.logger.info(f"AdditionWorksheet initialized with {num_problems} problems")

    def generate_problems(self):
        """
        Generate a list of addition problems using horizontal addition techniques.
        
        Returns:
            list: A list of formatted addition problems as strings.
        """
        self.logger.info(f"Generating {self.num_problems} addition problems")
        problems = []
        for _ in range(self.num_problems):
            a, b = self._generate_numbers()
            problem = f"{a} + {b} = "
            problems.append(problem)
            self.logger.debug(f"Generated problem: {problem}")
        return problems

    def _generate_numbers(self):
        """
        Generates two random numbers for an addition problem.

        Returns:
            tuple: A tuple containing two integers.
        """
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        self.logger.debug(f"Generated numbers: {a} and {b}")
        return a, b

    def display_problems(self):
        """
        Display the generated addition problems in a readable format.
        """
        self.logger.info("Displaying addition problems")
        problems = self.generate_problems()
        for problem in problems:
            print(problem)
        self.logger.info("Finished displaying problems")