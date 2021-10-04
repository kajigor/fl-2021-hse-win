import ply.lex as lex
import sys

tokens = [
  'NUM',
  'BACKSLASH',
  'DASH',
  'COMMA',
  'COLON',
  'ARROW',
  'DOTS',
  'STR'
]

t_BACKSLASH = r'\\'
t_DASH = r'-'
t_COMMA = r','
t_COLON = r':'
t_ARROW = r'->'
t_DOTS = r'\.\.\.'


t_ignore = ' \t'

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

def t_STR(t):
  r'"(?:[^\\"]|\\.)*"'
  t.value = t.value[1 : -1]
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()