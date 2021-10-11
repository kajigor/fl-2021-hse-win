import ply.yacc as yacc
import sys
from lex import tokens


def p_function_declaration(p):
    'Function_declaration : FUNCTION OPEN_CIRCULAR_BRACKET '


def p_error(p):
    print("Syntax error in input!")



def solve(file_name: str):
    parser = yacc.yacc()

    sys.stdin = open(file_name, 'r')
    sys.stdout = open(file_name + '.out', 'w')

    while True:
        try:
            s = input()
        except EOFError:
            break
        if not s:
            continue
        try:
            result = parser.parse(s)
        except Exception as e:
            break
