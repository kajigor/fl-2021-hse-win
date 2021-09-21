import ply.lex as lex
import sys

reserved = {
    'Alph': 'ALPH',
    'States': 'STATES',
    'Start_state': 'STARTSTATE',
    'Accept_states': 'ACCEPTSTATES',
    'Transits': 'TRANSITS'
}

tokens = [
  'NUM_OF_STATES',
  'VERTEX_NUM',
  'LETTER',
  'BEGIN_EDGE',
  'END_EDGE',
  'COMMA',
  'ROUND_BRACKET_OPENED',
  'ROUND_BRACKET_CLOSED',
  'EQ',
  'UNKNOWN_KEYWORD'
] + list(reserved.values())

def t_NUM_OF_STATES(t):
  r'(?<=States = )[0-9]+$'
  t.type = reserved.get(t.value, "NUM_OF_STATES")
  return t

def t_VERTEX_NUM(t):
  r'(?= )[0-9]+(?=[ \n])'
  t.type = reserved.get(t.value, 'VERTEX_NUM')
  return t

def t_LETTER(t):
  r'(?<= )\"[^\"]*"(?=[\n \)])'
  t.type = reserved.get(t.value, 'LETTER')
  return t

def t_BEGIN_EDGE(t):
  r'(?<=\()[0-9]+(?=,)'
  t.type = reserved.get(t.value, 'BEGIN_EDGE')
  return t

def t_END_EDGE(t):
  r'(?<=,\s)[0-9]+(?=,)'
  t.type = reserved.get(t.value, 'END_EDGE')
  return t

t_COMMA = r'\,'
t_ROUND_BRACKET_OPENED = r'\('
t_ROUND_BRACKET_CLOSED = r'\)'
t_EQ = r'='

def t_UNKNOWN_KEYWORD(t):
  r'[A-Za-z0-9_]+(?=\s=)'
  t.type = reserved.get(t.value, "UNKNOWN_KEYWORD")
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
