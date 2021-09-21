import ply.lex as lex
import sys

reserved = {
  '-->': 'EDGE',
  'state': 'STATE',
  'begin': 'BEGIN',
  'true': 'BOOL',
  'false': 'BOOL'
}

tokens = [
  'NUM',
  'WORD',
  'EDGE',
  'BOOL'
] + list(reserved.values())


def t_WORD(t):
  r'(begin)|(state)'
  t.type = reserved.get(t.value, 'WORD')
  return t

def t_BOOL(t):
  r'(true)|(false)'
  t.type = reserved.get(t.value, 'WORD')
  return t

def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

t_EDGE = r'-->'

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
