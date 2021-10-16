import matplotlib.pyplot as plt
import sys
#import generated_data
from recursive_parser import solve
from yacc import solve_yacc
from tests_generator import get_time_data


def run_tests(generate_new_data: bool = False):
    data_recursive = get_time_data(1)
    data_yacc = get_time_data(2)

    x_data_recursive = [elem[0] for elem in data_recursive]
    y_data_recursive = [elem[1] for elem in data_recursive]

    x_data_yacc = [elem[0] for elem in data_yacc]
    y_data_yacc = [elem[1] for elem in data_yacc]

    plt.title("Parsing time from number of symbols in input file dependency")
    plt.grid()
    plt.xlabel("Number of symbols in input file")
    plt.ylabel("Parsing time, microseconds")
    plt.scatter(x_data_recursive, y_data_recursive, label='recursive')
    plt.scatter(x_data_yacc, y_data_yacc, label='yacc')
    plt.legend()
    plt.show()

print("Insert file name: ")
file_name = input()
solve(file_name, False)
solve_yacc(file_name)
# run_tests()
