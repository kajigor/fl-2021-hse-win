# Author: Daniil Plotnikov (offdevil883@gmail.com) @ONdevil - telegram
import ply.lex as lex
import sys

reserved = {
  'Tuesday' : "IgotoUniversity"
}

tokens = [
  'UNKNOWN_KEYWORD',
  'AMOUNT_VERTEX',
  'VERTEX_NAME',
  'LETTER',
  'FROM_EDGE',
  'TO_EDGE',
  'VERTEX_CONDITION',
  'NUM',
  'DOLLAR',
  'ARROW',
  'COLON',
  'SEMICOLON',
  'COMMA',
  'CLOSE_BRACKET_FIGURE',
  'CLOSE_BRACKET_SQUARE',
  'BRACKET_VERTICAL'
] + list(reserved.values())

def t_UNKNOWN_KEYWORD(t):
  r'[A-Za-z0-9_]+\\n'
  t.type = reserved.get(t.value, "UNKNOWN_KEYWORD")
  return t

def t_AMOUNT_VERTEX(t):
  r'[0-9]+(?=\s})'
  t.type = reserved.get(t.value, "AMOUNT_VERTEX")
  return t

def t_VERTEX_NAME(t):
  r'[0-9a-zA-Z]+(?=\s])'
  t.type = reserved.get(t.value, 'VERTEX_NAME')
  return t

def t_VERTEX_CONDITION(t):
  r'(?<=->\s)[0-9]+(?=|)'
  t.type = reserved.get(t.value, 'VERTEX_CONDITION')
  return t

def t_FROM_EDGE(t):
  r'[0-9a-zA-Z]+(?=,)'
  t.type = reserved.get(t.value, 'FROM_EDGE')
  return t

def t_TO_EDGE(t):
  r'(?<=,)[0-9a-zA-Z]+'
  t.type = reserved.get(t.value, 'TO_EDGE')
  return t

def t_LETTER(t):
  r':*\b [0-9a-zA-Z]+(?=\$)'
  t.type = reserved.get(t.value, 'LETTER')
  return t

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

t_ARROW = r'->'
t_DOLLAR = r'\$'
t_COLON = r'\:' 
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_CLOSE_BRACKET_FIGURE = r'\}'
t_CLOSE_BRACKET_SQUARE = r'\]'
t_BRACKET_VERTICAL = r'\|'

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
