import ply.lex as lex
import sys

reserved = {
  'vertex': 'Start_new_vertex',
  'edge': 'Start_new_edge',
  'true': 'Is_Terminal',
  'false': 'Is_Not_Terminal',
}

tokens = [
  'VERTEXNAME',
  'SEMICOLON',
  'MOVE_TO',
  'COMMA',
  'CURLY_BRAKETS',
  'NUM'
] + list(reserved.values())

def t_VERTEXNAME(t):
  r'[a-z_][a-z_0-9]*'
  t.type = reserved.get(t.value, 'VERTEXNAME')
  return t

def t_MOVE_TO(t):
  r'\'.*?\''
  t.value = t.value[1 : -1]
  t.type = reserved.get(t.value, 'MOVE_TO')
  return t

t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_CURLY_BRAKETS = r'\{|\}'

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

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
