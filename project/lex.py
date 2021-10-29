import ply.lex as lex

reserved = {
    'if' : 'IF',
    'elif' : 'ELIF',
   'else' : 'ELSE',
   'while' : 'WHILE',
    'main' : 'MAIN',
    'null' : 'NULL',
    'return' : 'RETURN',
    'def' : 'DEF',
    'skip' : 'SKIP'
}

tokens = [
   'OPENCURLYBRACE',
   'CLOSECURLYBRACE',
   'OPENPAR',
   'CLOSEPAR',
   'NUM',
   'PLUS',
   'MINUS',
   'COMMA',
   'DIVMUL',
   'EQUAL',
   'NOTEQUAL',
   'COLON',
   'AND',
   'OR',
   'NOT',
   'LESS',
   'GREAT',
   'LESSEQUAL',
   'GREATEQUAL',
   'CARET',
   'ASSIGN',
   'VAR',
   'STRING'
] + list(reserved.values())

t_OPENCURLYBRACE = r'\{'
t_CLOSECURLYBRACE = r'\}'
t_OPENPAR = r'\('
t_CLOSEPAR = r'\)'
t_NUM = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_COMMA = r','
t_DIVMUL = r'/|\*'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_COLON = r';'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LESS = r'<'
t_GREAT = r'>'
t_LESSEQUAL = r'<='
t_GREATEQUAL = r'>='
t_CARET = r'\^'
t_ASSIGN = r'='

t_ignore  = ' \t'

def t_STRING(t):
  r'"[^"\\]*(?:\\.[^"\\]*)*"'
  t.value = t.value[1 : -1]
  return t

def t_VAR(t):
    r'([a-zA-Z][_0-9A-Za-z]*)'
    t.type = reserved.get(t.value,'VAR')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    exit()

lexer = lex.lex()
