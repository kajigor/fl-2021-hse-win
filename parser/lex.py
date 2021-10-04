import ply.lex as lex
import sys

tokens = [
  'TERM',
  'ALPHABET',
  'START',
  'LIST',
  'STATES',
  'NUM',
  'VERTICAL_LINE',
  'COMMA',
  'OPEN_BRACKET',
  'CLOSE_BRACKET',
  'ARROW',
  'COLON',
  'WORD',
  'VERTEX_TO',
  'VERTEX_FROM',
  'POINT_COMMA'
] 

def t_START(t):
  r'Start'
  return t
def t_STATES(t):
  r'States'
  return t  
def t_ALPHABET(t):
  r'Alphabet'
  return t
def t_LIST(t):
  r'List'
  return t 
def t_TERM(t):
  r'Term'
  return t   
def t_WORD(t):
  r'\'.*?\''
  t.value = t.value[1: -1]
  return t
def t_VERTEX_TO(t):
  r'\([\d]+;'
  t.value = t.value[1: -1]
  return t
def t_VERTEX_FROM(t):
  r'[\d]+:'
  t.value = t.value[:-1]
  return t  
def t_NUM(t):
  r'((-?[1-9][0-9]*)|0)'
  t.value = int(t.value)
  return t
  
t_POINT_COMMA=r'\;'
t_COMMA =r'\,'  
t_ARROW = r'\-\>'
t_COLON = r'\:'
t_VERTICAL_LINE = r'\|'
t_OPEN_BRACKET = r'\('
t_CLOSE_BRACKET = r'\)'
t_ignore = ' \t'


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()
with open(sys.argv[1], 'r') as f:
  input=f.read()
lexer.input(input)
sys.stdout = open(sys.argv[1] + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)