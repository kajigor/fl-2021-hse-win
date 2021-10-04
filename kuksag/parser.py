import ply.yacc as yacc
from lexer import *
import base


def p_expression_vertices(p):
    'expression : VERTICES NUM'
    p[0] = p[2]


def p_expression_edges(p):
    'expression : EDGES NUM'
    p[0] = p[2]


def p_expression_edge(p):
    'expression : FROM NUM TO NUM EDGE EDGE_VALUE'
    p[0] = p[2] * p[4]
    p[0] = base.Edge(vertex_from=p[1], vertex_to=[3], edge_value=p[6])


def p_expression_terminal(p):
    'expression : TERMINAL NUM'
    p[0] = p[2]


def p_expression_root(p):
    'expression : START NUM'
    p[0] = p[2]


def p_error(p):
    print("Syntax error")


def parse(line, log=None):
    parser = yacc.yacc()
    if not check_line(line, log):
        return False
    return parser.parse(line)


