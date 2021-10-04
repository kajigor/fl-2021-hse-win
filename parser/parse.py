import sys

import ply.yacc as yacc

from lex import tokens

# automata -- sigma q start terminal delta in this order

ERROR = False


def p_automata(p):
    'automata : sigma q start terminal delta'
    p[0] = {'sigma': p[1], 'q': p[2], 'start': p[3], 'terminals': p[4], 'delta': p[5]}


def p_vertex_num(p):
    'vertex : NUM'
    p[0] = p[1]


def p_vertexes_one(p):
    'vertexes : vertex'
    p[0] = [p[1]]


def p_vertexes_multiple(p):
    'vertexes : NUM SEP vertexes'
    p[0] = [p[1]] + p[3]


def p_terminals(p):
    'terminal : TERMINAL vertexes'
    p[0] = p[2]


def p_sigma(p):
    'sigma : SIGMA vertexes'
    p[0] = p[2]


def p_q(p):
    'q : STATES vertexes'
    p[0] = p[2]


def p_start(p):
    'start : START vertex'
    p[0] = p[2]


def p_expression(p):
    'expression : OPEN_BR NUM SEP NUM CLOSED_BR ARRFUNC NUM'
    p[0] = {"start_state": p[2], "symbol": p[4], "final_state": p[7]}


def p_expressions_one(p):
    'expressions : expression'
    p[0] = [p[1]]


def p_expression_multi(p):
    'expressions : expression SEP expressions'
    p[0] = [p[1]] + p[3]


def p_delta(p):
    'delta : DELTA expressions'
    p[0] = p[2]


def p_unexpected_id(p):
    'uid : UNEXPECTED_ID'
    global ERROR
    ERROR = True


def p_error(p):
    global ERROR
    ERROR = True
    sys.stderr.write("Syntax error -- unexpected symbol " + str(p.value))


parser = yacc.yacc()
fin = open(sys.argv[1], 'r')
result = parser.parse(fin.read())
fin.close()
fout = open(sys.argv[1] + '.out', 'w')
if (not ERROR):
    fout.write(str(result))
