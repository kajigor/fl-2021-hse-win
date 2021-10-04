import sys

import ply.yacc as yacc

from lex import tokens


# if 42 then (if 0 then 777 else 9)


# def p_if(p):
#   '''if : IF expression THEN if ELSE if
#         | IF expression THEN if
#         | expression '''
#   if len(p) == 7:
#     p[0] = p[4] if p[2] == 0 else p[6]
#   else:
#     if len(p) == 5:
#       if p[2] == 0 :
#         p[0] = p[4]
#     else:
#       p[0] = p[1]
#
# def p_expression_plus(p):
#   'expression : expression PLUS expression'
#   p[0] = p[1] - p[3]
#
# def p_expression_term(p):
#   'expression : term'
#   p[0] = p[1]
# #
# def p_term_times(p):
#   'term : term MULT factor'
#   p[0] = p[1] * p[3]
# #
# def p_term_factor(p):
#   'term : factor'
#   p[0] = p[1]
#
# def p_factor_num(p):
#   'factor : NUM'
#   p[0] = p[1]
#
# def p_factor_expr(p):
#   'factor : LBR expression RBR'
#   p[0] = p[2]

class Automate:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append(str(part))
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

def p_automate(p):
    '''automate : states start end alphabet function'''
    p[0] = Automate("AUTOMATE", p[1:])

def p_states_definition(p):
    'states_definition : EQUAL BRACKET state_list BRACKET SEMICOLON '
    p[0] = p[3]

def p_states(p):
    'states : STATES states_definition'
    p[0] = Automate("STATES", p[2])

def p_start(p):
    'start : START states_definition'
    p[0] = Automate("START", p[2])

def p_end(p):
    'end : END states_definition'
    p[0] = Automate("END", p[2])

def p_error(p):
    print("Syntax error")


def p_state_list(p):
    '''state_list : state state_list
                  | state'''
    p[0] = []
    p[0] += [p[1]]
    if (len(p) == 3):
        p[0] += p[2]

def p_state(p):
    'state : STATE'
    p[0] = p[1]


def p_transfer(p):
    'transfer : TRANSFER'
    p[0] = p[1]


def p_transfer_list(p):
    '''transfer_list : transfer transfer_list
                     | transfer'''
    p[0] = []
    p[0] += [p[1]]
    if (len(p) == 3):
        p[0] += p[2]

def p_alphabet_definition(p):
    'alphabet_definition : EQUAL BRACKET transfer_list BRACKET SEMICOLON'
    p[0] = p[3]

def p_alphabet(p):
    'alphabet : ALPHABET alphabet_definition'
    p[0] = Automate("ALPHABET", p[2])

def p_function(p):
    'function : FUNCTION function_def'
    p[0] = Automate("FUNCTION", p[2])

def p_function_def(p):
    'function_def : EQUAL BRACKET function_list BRACKET SEMICOLON'
    p[0] = p[3]

def p_where(p):
    'where : state transfer state'
    p[0] = p[1] + " --(" + p[2] + ")--> " + p[3]

def p_function_list(p):
    '''function_list : where function_list
                     | where'''
    p[0] = []
    p[0] += [p[1]]
    if (len(p) == 3):
        p[0] += p[2]

sys.stdout = open(sys.argv[1] + '.out', 'w')

parser = yacc.yacc()
s = open(sys.argv[1], 'r').read()
# while True:
# try:
#   s = input("calc> ")
# except EOFError:
#   break
# if not s:
# continue
result = parser.parse(s)
print(result)
