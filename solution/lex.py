import ply.lex as lex
import sys
reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'skip' : 'SKIP',
   'void' : 'VOID',
   'return' : 'RETURN',
   'while' : 'WHILE',
   'begin' : 'BEGIN',
   'end' : 'END',
   'null' : 'NULL',
   'main' : 'MAIN'

}
tokens =   [
  'SEMICOLON', 'COMMA', 'ASSIGNMENT', 'CARET', 'MINUS', 'MULT', 'DIV', 'PLUS', 'EQUAL', 'NOTEQUAL',
  'LESSEQUAL', 'GREATEQUAL', 'LESS', 'GREAT', 'NOT', 'AND', 'OR', 'BRACKET_OPEN', "BRACKET_CLOSE",
  'NUMBER', 'STRING', 'VARIABLE', 'FUNCTION_NAME'
] + list(reserved.values())

t_ignore = ' \t'
t_SEMICOLON =r';'
t_COMMA = r','
t_ASSIGNMENT = r':='
t_CARET = r'\^'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'\/'
t_PLUS = r'\+'
t_EQUAL = r'=='
t_NOTEQUAL = r'\/='
t_LESSEQUAL = r'<='
t_GREATEQUAL = r'>='
t_LESS = r'<'
t_GREAT = r'>'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_BRACKET_OPEN = r'\('
t_BRACKET_CLOSE = r'\)'
t_NUMBER = r'[1-9][0-9]*|0'
def t_STRING(t):
  r'"[^"\\]*(?:\\.[^"\\]*)*"'
  t.value = t.value[1 : -1]
  return t
def t_VARIABLE(t):
  r'([a-z][_0-9A-Za-z]*)'
  t.type = reserved.get(t.value,'VARIABLE')
  return t
t_FUNCTION_NAME = r'([A-Z][_0-9A-Za-z]*)'
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  exit()
lexer = lex.lex()
