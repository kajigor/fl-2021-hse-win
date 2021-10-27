from lex import tokens
import ply.yacc as yacc

class Node:
    def parts_str(self):
        st = []
        for part in self.parts:
            st.append( str( part ) )
        return "\n".join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts_str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self

    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

precedence = (
    ('right', 'AND', 'OR'),
    ('nonassoc', 'NOT'),
    ('nonassoc', 'EQUAL', 'NOTEQUAL', 'LESSEQUAL', 'GREATEQUAL', 'LESS', 'GREAT'),
    ('left', 'PLUS'),
    ('left', 'MINUS'),
    ('left', 'DIVMUL'),
    ('right', 'CARET')
)

def p_error(p):
  print('unidentified token', p)
  exit()

def p_body(p):
    '''body : main
            | functions main'''

def p_functions(p):
    '''functions : functions
                 | function'''

def p_function(p):
    '''function : VOID VAR OPENPAR CLOSEPAR block
                | VOID VAR OPENPAR args CLOSEPAR block'''

def p_block(p):
    '''block : OPENCURLYBRACE operator CLOSECURLYBRACE'''

def p_args(p):
    '''args : args COMMA VAR
            | VAR'''

def p_operator(p):
    '''operator : operators
                | SKIP COLON
                | if
                | while
                | assign COLON
                | func_call COLON
                | return'''
    
def p_operators(p):
    '''operators : operator
                 | operators operator'''

def p_if(p):
    '''if : IF condition block branches ELSE block
          | IF condition block ELSE block
          | IF condition block'''

def p_branches(p):
    '''branches : branches ELIF condition block
                | ELIF condition block'''

def p_condition(p):
    '''condition : OPENPAR expr CLOSEPAR'''

def p_expr(p):
    '''expr : NUM
            | STRING
            | VAR
            | NULL
            | func_call
            | expr CARET expr
            | MINUS expr
            | expr DIVMUL expr
            | expr PLUS expr
            | expr MINUS expr
            | expr EQUAL expr
            | expr NOTEQUAL expr
            | expr LESSEQUAL expr
            | expr GREATEQUAL expr
            | expr LESS expr
            | expr GREAT expr
            | NOT expr
            | expr AND expr
            | expr OR expr'''
    
def p_while(p):
    '''while : WHILE condition block'''

def p_assign(p):
    '''assign : VAR ASSIGN expr'''

def p_func_call(p):
    '''func_call : VAR OPENPAR CLOSEPAR
                 | VAR OPENPAR args CLOSEPAR'''

def p_return(p):
    '''return : RETURN expr'''

def p_main(p):
    '''main : MAIN OPENPAR CLOSEPAR block'''
    
parser = yacc.yacc()

def build_tree(code):
    return parser.parse(code)
