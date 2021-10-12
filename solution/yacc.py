import ply.yacc as yacc
import sys
from lex import tokens

precedence = (
    ('right', 'OR'),
    ('right', 'AND'),
    ('nonassoc', 'NOT'),
    ('nonassoc', 'EQUAL', 'NONEQUAL', 'LEQ', 'GEQ', 'LE', 'GE'),
    ('right', 'LINKING_OPERATOR'),
    ('nonassoc', 'ASSIGNMENT_OPERATOR'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'POW'),
)


def p_code(p):
    '''code : code func_decl
            | func_decl'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_function_declaration_with_args(p):
    '''func_decl : FUNCTION_DEFINITION FUNCTION OPEN_CIRC_BR decl_args_list CLOSE_CIRC_BR body'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + "{" + p[6] + "}"
    print("Function: " + p[2] + ", arity: " + str(p[4].count(',') + 1))
    print(p[6])


def p_function_declaration_without_args(p):
    '''func_decl : FUNCTION_DEFINITION FUNCTION OPEN_CIRC_BR CLOSE_CIRC_BR body'''
    print("Function: " + p[2] + ", arity: 0")


def p_read_decl_args(p):
    '''decl_args_list : decl_args_list COMMA TYPE_INT VARIABLE
                   | decl_args_list COMMA TYPE_CHAR VARIABLE
                   | decl_args_list COMMA TYPE_STRING VARIABLE
                   | decl_args_list COMMA TYPE_BOOLEAN VARIABLE
                   | TYPE_INT VARIABLE
                   | TYPE_CHAR VARIABLE
                   | TYPE_STRING VARIABLE
                   | TYPE_BOOLEAN VARIABLE'''
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = p[1] + p[2]


def p_read_decl(p):
    '''args_list : args_list COMMA VARIABLE
                 | VARIABLE '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2] + p[3]


def p_conditional_first_part(p):
    '''expression : CONDITIONAL_OPERATOR_IF OPEN_CIRC_BR logic_expression CLOSE_CIRC_BR body'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_cycle(p):
    '''expression : CYCLE_OPERATOR OPEN_CIRC_BR logic_expression CLOSE_CIRC_BR body'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5]


def p_body(p):
    'body : OPEN_SHAPED_BR expression CLOSE_SHAPED_BR'
    p[0] = p[1] + p[2] + p[3]


def p_expression_link(p):
    '''expression : expression LINKING_OPERATOR expression
                  | expression LINKING_OPERATOR'''
    if len(p) == 3:
        p[0] = str(p[1]) + str(p[2])
    else:
        p[0] = str(p[1]) + p[2] + str(p[3])


def p_declaration(p):
    '''expression : VARIABLE ASSIGNMENT_OPERATOR expression'''
    p[0] = p[1] + p[2] + str(p[3])


def p_bool_expression(p):
    '''logic_expression : expression EQUAL expression
                  | expression NONEQUAL expression
                  | expression LEQ expression
                  | expression LE expression
                  | expression GEQ expression
                  | expression GE expression
                  | NOT expression
                  | expression AND expression
                  | expression OR expression '''
    if len(p) == 3:
        p[0] = p[1] + str(p[2])
    else:
        p[0] = str(p[1]) + p[2] + str(p[3])


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_function_call_with_args(p):
    'factor : FUNCTION OPEN_CIRC_BR  CLOSE_CIRC_BR'
    p[0] = p[1] + p[2] + p[3]


def p_function_call_without_args(p):
    'factor : FUNCTION OPEN_CIRC_BR args_list CLOSE_CIRC_BR'
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_factor_variable(p):
    'factor : VARIABLE'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : OPEN_CIRC_BR expression CLOSE_CIRC_BR'
    p[0] = p[2]


def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]


def p_error(p):
    if p:
        print("Syntax error at token", p.type)
    else:
        print("Syntax error at EOF")


def solve(file_name: str):
    parser = yacc.yacc()
    f = open(file_name, 'r')
    s = f.read()
    f.close()
    sys.stdout = open(file_name + '.out', 'w')
    result = parser.parse(s)
