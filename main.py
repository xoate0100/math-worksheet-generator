import argparse
from src.worksheet_factory import WorksheetFactory

def main():
    """
    Main function to run the math worksheet generator.
    """
    parser = argparse.ArgumentParser(description="Generate math worksheets for addition or subtraction.")
    parser.add_argument("type", choices=["addition", "subtraction"], help="Type of math worksheet to generate")
    parser.add_argument("--problems", type=int, default=10, help="Number of problems to generate (default: 10)")
    args = parser.parse_args()

    try:
        worksheet = WorksheetFactory.get_worksheet(args.type, args.problems)
        print(f"Generating {args.problems} {args.type} problems:\n")
        worksheet.display_problems()
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())