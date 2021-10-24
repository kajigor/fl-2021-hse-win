import ply.yacc as yacc
import sys
from lex import tokens, run_lexer


class Node():
    # name is a string with info about expr
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.children = []  # the list of children that are Nodes

    def app_child(self, child):
        self.children.append(child)

    def ins_child(self, child):
        self.children.insert(0, child)


def print_tree(a, tabs):
    print("  " * tabs + a.type + a.value)
    for ch in a.children:
        print_tree(ch, tabs + 1)


code_versions_list = []

# parsing part

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
        p[1].app_child(p[2])
        p[0] = p[1]
        code_versions_list.append(p[0])
    else:
        p[0] = Node("root", "")
        p[0].app_child(p[1])
        code_versions_list.append(p[0])


def p_function_declaration_with_args(p):
    '''func_decl : FUNCTION_DEFINITION FUNCTION OPEN_CIRC_BR decl_args_list CLOSE_CIRC_BR body'''
    p[0] = Node("Function declaration", "")
    p[0].app_child(Node("Function name: ", p[2]))
    p[0].app_child(Node("Function arity: ", str(len(p[4].children))))
    p[0].app_child(p[4])
    p[0].app_child(p[6])


def p_function_declaration_without_args(p):
    '''func_decl : FUNCTION_DEFINITION FUNCTION OPEN_CIRC_BR CLOSE_CIRC_BR body'''
    p[0] = Node("Function declaration")
    p[0].app_child(Node("Function name: ", p[2]))
    p[0].app_child(Node("Function arity: ", "0"))
    p[0].app_child(p[5])


def p_read_decl_args(p):
    '''decl_args_list : decl_args_list COMMA var_def
                      | var_def '''
    if len(p) == 4:
        p[1].app_child(p[3])
        p[0] = p[1]
    else:
        p[0] = Node("func declaration args", "")
        p[0].app_child(p[1])


def p_read_decl(p):
    '''args_list : args_list COMMA factor
                 | factor '''
    if len(p) == 2:
        p[0] = Node("arguments list", "")
        p[0].app_child(p[1])
    else:
        p[1].app_child(p[3])
        p[0] = p[1]


def p_conditional(p):
    '''expression : fst_part
                  | fst_part snd_part'''
    p[0] = Node("conditional", "")
    if len(p) == 2:
        p[0].app_child(p[1])
    else:
        p[0].app_child(p[1])
        p[0].app_child(p[2])


def p_conditional_snd_part(p):
    '''snd_part : CONDITIONAL_OPERATOR_ELSE body'''
    p[0] = Node("else", "")
    p[0].app_child(p[2])


def p_conditional_first_part(p):
    '''fst_part : CONDITIONAL_OPERATOR_IF OPEN_CIRC_BR expression CLOSE_CIRC_BR body'''
    p[0] = Node("if", "")
    p[0].app_child(p[3])
    p[0].app_child(p[5])


def p_cycle(p):
    '''expression : CYCLE_OPERATOR OPEN_CIRC_BR expression CLOSE_CIRC_BR body'''
    p[0] = Node("cycle", "")
    p[0].app_child(p[3])
    p[0].app_child(p[5])


def p_body(p):
    'body : OPEN_SHAPED_BR expression CLOSE_SHAPED_BR'
    p[0] = Node("body", "")
    p[0].app_child(p[2])


def p_expression_link(p):
    '''expression : expression LINKING_OPERATOR expression
                  | expression LINKING_OPERATOR'''
    if len(p) == 3:
        p[0] = Node("last expression", "")
        p[0].app_child(p[1])
    else:
        p[0] = Node("expression link", "")
        p[0].app_child(p[1])
        p[0].app_child(Node("linking operator: ", ";"))
        p[0].app_child(p[3])


def p_declaration(p):
    '''expression : VARIABLE ASSIGNMENT_OPERATOR expression
                  | var_def ASSIGNMENT_OPERATOR expression'''
    p[0] = Node("assignment", "")
    if type(p[1]) is Node:
        p[0].app_child(p[1])
    else:
        p[0].app_child(Node("variable: ", p[1]))
    p[0].app_child(Node("", p[2]))
    p[0].app_child(p[3])


def p_bool_expression(p):
    '''expression : expression EQUAL expression
                  | expression NONEQUAL expression
                  | expression LEQ expression
                  | expression LE expression
                  | expression GEQ expression
                  | expression GE expression
                  | NOT expression
                  | expression AND expression
                  | expression OR expression '''
    p[0] = Node("bool expression", "")
    if len(p) == 3:
        p[0].app_child(Node("bool operator: ", p[1]))
    else:
        p[0].app_child(p[1])
        p[0].app_child(Node("bool operator: ", p[2]))
        p[0].app_child(p[3])


def p_expression_plus(p):
    '''expression : expression PLUS term
                  | expression INCREMENT term'''
    p[0] = Node("plus", "")
    p[0].app_child(p[1])
    p[0].app_child(p[3])


def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = Node("minus", "")
    p[0].app_child(p[1])
    p[0].app_child(p[3])


def p_return_expression(p):
    'expression : END_OF_FUNCTION expression'
    p[0] = Node("return", "")
    p[0].app_child(p[2])


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = Node("times", "")
    p[0].app_child(p[1])
    p[0].app_child(p[3])


def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = Node("divide", "")
    p[0].app_child(p[1])
    p[0].app_child(p[3])


def p_term_pow(p):
    'term : term POW factor'
    p[0] = Node("pow", "")
    p[0].app_child(p[1])
    p[0].app_child(p[3])


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_function_call_without_args(p):
    'factor : FUNCTION OPEN_CIRC_BR CLOSE_CIRC_BR'
    p[0] = Node("call function: ", p[1])


def p_function_call_with_args(p):
    'factor : FUNCTION OPEN_CIRC_BR args_list CLOSE_CIRC_BR'
    p[0] = Node("call function: ", p[1])
    p[0].app_child(p[3])


def p_factor_char_or_string(p):
    'factor : QUOT expression QUOT'
    p[0] = Node("string: ", p[1] + str(p[2]) + p[3])


def p_var_definition(p):
    '''var_def : TYPE_INT VARIABLE
            | TYPE_CHAR VARIABLE
            | TYPE_STRING VARIABLE
            | TYPE_BOOLEAN VARIABLE'''
    p[0] = Node("variable definition: ", "")
    p[0].app_child(Node("type: ", p[1]))
    p[0].app_child(Node("variable: ", p[2]))


def p_factor_variable(p):
    '''factor : VARIABLE'''
    p[0] = Node("variable: ", p[1])


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = Node("number: ", str(p[1]))


def p_factor_expr(p):
    'factor : OPEN_CIRC_BR expression CLOSE_CIRC_BR'
    p[0] = Node("expression", "")
    p[0].app_child(p[2])


def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = Node("-", p[2].value)


def p_error(p):
    if p:
        print("Syntax error at token", p.type)
    else:
        print("Syntax error at EOF")


def solve_yacc(file_name: str):
    run_lexer(file_name)
    parser = yacc.yacc()
    f = open(file_name, 'r')
    s = f.read()
    f.close()
    sys.stdout = open(file_name + '.out', 'w')
    print("Yacc parser output:")
    result = parser.parse(s)
    print_tree(code_versions_list[len(code_versions_list) - 1], 0)
