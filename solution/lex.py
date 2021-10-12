import ply.lex as lex
import sys

reserved = {
    'if': 'CONDITIONAL_OPERATOR_IF',
    'else': 'CONDITIONAL_OPERATOR_ELSE',
    'while': 'CYCLE_OPERATOR',
    'int': 'TYPE_INT',
    'char': 'TYPE_CHAR',
    'string': 'TYPE_STRING',
    'bool': 'TYPE_BOOLEAN',
    'main': 'MAIN',
    'return': 'END_OF_FUNCTION',
    'def': 'FUNCTION_DEFINITION'
}

tokens = [
             'NUMBER',
             'FUNCTION',
             'VARIABLE',
             'PLUS',
             'INCREMENT',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'OPEN_CIRC_BR',
             'CLOSE_CIRC_BR',
             'OPEN_SHAPED_BR',
             'CLOSE_SHAPED_BR',
             'LINKING_OPERATOR',
             'POW',
             'EQUAL',
             'NONEQUAL',
             'LEQ',
             'LE',
             'GEQ',
             'GE',
             'NOT',
             'AND',
             'OR',
             'ASSIGNMENT_OPERATOR',
             'COMMA',
             'QUOT'
         ] + list(reserved.values())

t_PLUS = r'\+'
t_INCREMENT = r'\+='
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_OPEN_CIRC_BR = r'\('
t_CLOSE_CIRC_BR = r'\)'
t_OPEN_SHAPED_BR = r'\{'
t_CLOSE_SHAPED_BR = r'\}'
t_LINKING_OPERATOR = r'\;'
t_POW = r'\^'
t_EQUAL = r'\=='
t_NONEQUAL = r'\\='
t_LEQ = r'\<='
t_LE = r'\<'
t_GEQ = r'\>='
t_GE = r'\>'
t_NOT = r'\!'
t_AND = r'\&&'
t_OR = r'\|\|'
t_ASSIGNMENT_OPERATOR = r'\:'
t_COMMA = r'\,'
t_QUOT = r'\''

t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FUNCTION(t):
    r'((?<=def\s)[A-Za-z0-9]+)|([A-Za-z0-9]+(?=\())'
    t.type = reserved.get(t.value, "FUNCTION")
    return t


def t_VARIABLE(t):
    r'[A-Za-z0-9]+'
    t.type = reserved.get(t.value, "VARIABLE")
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
# sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)