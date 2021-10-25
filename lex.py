import ply.lex as lex
import sys

reserved = {
    'define': 'DEFINE',
    'do': 'DO',
    'for': 'FOR',
    'make': 'MAKE',
    'from': 'FROM'
}

tokens = ['KEYWORD',
          'FUNCTION',
          'CONSTRUCTOR',
          'EQ',
          'OR',
          'AND',
          'COMMENT',
          'VARIABLE',
          'LBR',
          'RBR',
          'newline'] + list(reserved.values())

def t_KEYWORD(t):
    r'\s*(define|do|for|make|from)\s*'
    t.type = reserved.get(t.value.strip(), 'KEYWORD')
    t.value = t.value.strip()
    return t

def t_FUNCTION(t):
    r'\s*\#[A-z]+[A-z|0-9]*\s*'
    t.value = t.value.strip()
    return t

def t_CONSTRUCTOR(t):
    r'\s*\%[A-z]+[A-z|0-9]*\s*'
    t.value = t.value.strip()
    return t

def t_EQ(t):
    r'\s*\?\=\s*'
    t.value = t.value.strip()
    return t

def t_OR(t):
    r'\s*\+\s*'
    t.value = t.value.strip()
    return t

def t_AND(t):
    r'\s*\*\s*'
    t.value = t.value.strip()
    return t

def t_COMMENT(t):
    r'\s*\|\|.+\s*'
    t.value = t.value.strip()
    return t

def t_VARIABLE(t):
    r'\s*[A-z]+[A-z|0-9]*\s*'
    t.value = t.value.strip()
    return t

def t_LBR(t):
    r'\s*\(\s*'
    t.value = t.value.strip()
    return t

def t_RBR(t):
    r'\s*\)\s*'
    t.value = t.value.strip()
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


def t_error(t):
    print("Illegal character in " + t.value)
    exit()


lexer = lex.lex()