from src.addition_worksheet import AdditionWorksheet

class WorksheetFactory:
    """Factory class to handle the creation of different types of worksheets."""
    
    @staticmethod
    def get_worksheet(worksheet_type: str, num_problems: int):
        """
        Factory method to return the appropriate worksheet object based on the type.
        
        Args:
            worksheet_type (str): The type of worksheet (e.g., "addition").
            num_problems (int): The number of problems for the worksheet.
        
        Returns:
            object: An instance of a worksheet class.
        
        Raises:
            ValueError: If the worksheet_type is unsupported.
        """
        if worksheet_type == "addition":
            return AdditionWorksheet(num_problems)
        else:
            raise ValueError(f"Unsupported worksheet type: {worksheet_type}")
