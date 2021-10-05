import ply.lex as lex
import sys

reserved = {
  'Alphabet': 'ALPHABET',
  'Q': 'Q',
  'start': 'START',
  'runoff' : 'RUNOFF',
  'T' : 'T',
  'edges' : 'EDGES'
}

tokens = [
  'NUM',
  'DASH',
  'COLON',
  'OPARENTHESES',
  'CPARENTHESES',
  'COMMA',
  'SEMICOLON',
  'SYMBOL'
] + list(reserved.values())


def t_NUM(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

t_DASH = r'--'
t_COLON = r':'
t_OPARENTHESES = r'\('
t_CPARENTHESES = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'
t_ALPHABET = r'Alphabet'
t_Q = r'Q'
t_START = r'start'
t_RUNOFF = r'runoff'
t_T = r'T'
t_EDGES = r'edges'

def t_SYMBOL(t):
  r'"(?:[a-z_0-9]|\\.| |[^\\"])*"'
  t.value = t.value[1 : -1] #выводим содержимое без кавычек
  return t


t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

#lexer.input(open(sys.argv[1], 'r').read())
#sys.stdout = open(sys.argv[1] + '.out', 'w')
# lexer.input(sys.argv[1])

#while True:
  #tok = lexer.token()
  #if not tok:
    #break
  #print(tok)