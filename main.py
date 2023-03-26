from openpyxl import Workbook, load_workbook
from Colors import *
import Average
import Maximum
import Minimum

print(f"{Colors.OKCYAN}Hello User!!{Colors.ENDC}")

function_user_input = int(input(f"{Colors.HEADER}1.Calculate Average\n"
                                "2.Calculate Max\n"
                                "3.Calculate Min\n"
                                f"4.Calculate Sum\n{Colors.ENDC}"))

file_name_user_input = input(
    f"Enter the name of the{Colors.WARNING}{Colors.BOLD} file {Colors.ENDC}{Colors.ENDC}you want to work on: ")
sheet_name_user_input = input(
    f"Enter the name of the{Colors.WARNING}{Colors.BOLD} sheet {Colors.ENDC}{Colors.ENDC}you want to work on: ")
column_user_input = input(
    f"Enter the{Colors.WARNING}{Colors.BOLD} column {Colors.ENDC}{Colors.ENDC}you want to work on: ")

# Load WorkBook for the file we want to work on
wb = load_workbook(file_name_user_input)
ws = wb.activate
