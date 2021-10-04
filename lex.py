import ply.lex as lex
import sys
import re

tokens = [
  'EDGE',
  'VERTEX',
  'TERMINAL',
  'ARROW',
  'COLON',
  'QUOTES',
  'SEMICOLON',
  'NUM'
]
def t_EDGE(t):
  r'"(.)+"(?=\n)'
  t.value = t.value[1:-1].replace('\\\\', '\\')
  return t
t_VERTEX = r'Q([1-9][0-9]*|0)'
t_TERMINAL = r'T([1-9][0-9]*|0)'
t_ARROW = r'->'
t_COLON = r':'
t_QUOTES = r'"'
t_SEMICOLON = r';'
t_NUM = r'([1-9][0-9]*|0)'
t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()
fin = open(sys.argv[1], 'r')
lexer.input(fin.read())
fin.close()
fout = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  fout.write(str(tok)+'\n')
fout.close()
