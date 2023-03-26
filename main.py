import  Average

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{Colors.OKCYAN}Hello User!!{Colors.ENDC}")

user_input = int(input(f"{Colors.BOLD}1.Calculate Average\n"
                       "2.Calculate Max\n"
                       "3.Calculate Min\n"
                       "4.Calculate\n"))


avg = Average.calculate_average([1,2,3,4])
print(avg)