from lex import tokens
import ply.yacc as yacc
import sys

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
    if len(p) == 2:
        p[0] = Node('file', [p[1]])
    else:
        p[0] = Node('file', [p[1],p[2]])

def p_functions(p):
    '''functions : functions function
                 | function'''
    if len(p) == 3:
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node ('function definitions', [p[1]])

def p_function(p):
    '''function : DEF VAR OPENPAR CLOSEPAR block
                | DEF VAR OPENPAR args CLOSEPAR block'''
    if len(p) == 6:
        p[0] = Node('function definition', [Node('name', [p[2]]), p[5]])
    else:
        p[0] = Node('function definition', [Node('name', [p[2]]), p[4], p[6]])

def p_block(p):
    '''block : OPENCURLYBRACE operators CLOSECURLYBRACE
             | OPENCURLYBRACE CLOSECURLYBRACE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = Node('body', [])

def p_args(p):
    '''args : args COMMA VAR
            | VAR'''
    if len(p) == 4:
        p[0] = p[1].add_parts([p[3]])
    else:
        p[0] = Node('arguments', [p[1]])

def p_operator(p):
    '''operator : SKIP COLON
                | if
                | while
                | assign COLON
                | func_call COLON
                | return COLON'''
    p[0] = p[1]

def p_operators(p):
    '''operators : operator
                | operators operator'''
    if len(p) == 2:
        p[0] = Node('body', [p[1]])
    else:
        p[0] = p[1].add_parts([p[2]])

def p_if(p):
    '''if : IF condition block branches ELSE block
          | IF condition block ELSE block
          | IF condition block'''
    if len(p) == 7:
        p[0] = Node('conditional operator', [Node('if', [p[2], p[3]]), p[4], Node('else', [p[6]])])
    elif len(p) == 6:
        p[0] = Node('conditional operator', [Node('if', [p[2], p[3]]), Node('else', [p[5]])])
    else:
        p[0] = Node('conditional operator', [Node('if', [p[2], p[3]])])

def p_branches(p):
    '''branches : branches ELIF condition block
                | ELIF condition block'''
    if len(p) == 5:
        p[0] = p[1].add_parts([p[3], p[4]])
    else:
        p[0] = Node('elif', [p[2], p[3]])

def p_condition(p):
    '''condition : OPENPAR expr CLOSEPAR'''
    p[0] = Node('condition', [p[2]])

def p_expr(p):
    '''expr : expr CARET expr
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
    if len(p) == 3:
        p[0] = Node(p[1], [p[2]])
    else:
        p[0]= Node('expression', [Node(p[2], [p[1], p[3]])])

def p_expr_num(p):
    '''expr : NUM'''
    if (len(p) == 2):
        p[0] = Node('number', [p[1]])

def p_expr_binnum(p):
    '''expr : BINNUM'''
    if (len(p) == 2):
        p[0] = Node('binary number', [p[1]])

def p_expr_null(p):
    '''expr : NULL'''
    if (len(p) == 2):
        p[0] = Node('null', [p[1]])

def p_expr_string(p):
    '''expr : STRING'''
    if (len(p) == 2):
        p[0] = Node('string', [p[1]])

def p_expr_var(p):
    '''expr : VAR'''
    if (len(p) == 2):
        p[0] = Node('variable', [p[1]])

def p_expr_func_call(p):
    '''expr : func_call'''
    if (len(p) == 2):
        p[0] = p[1]
    
def p_while(p):
    '''while : WHILE condition block'''
    p[0] = Node('loop statement', [p[2], p[3]])

def p_assign(p):
    '''assign : VAR ASSIGN expr'''
    p[0] = Node('assignment', [Node ('variable', [p[1]]), p[3]])

def p_func_call(p):
    '''func_call : VAR OPENPAR CLOSEPAR
                 | VAR OPENPAR call_args CLOSEPAR'''
    if len(p) == 4:
        p[0] = Node('function call', [Node('name', [p[1]]), Node('args', [])])
    else:
        p[0] = Node('function call', [Node('name', [p[1]]), p[3]])

def p_call_args(p):
    '''call_args : call_args COMMA expr
                 | expr'''
    if len(p) == 4:
        p[0] = p[1].add_parts([p[3]])
    else:
        p[0] = Node('args', [p[1]])

def p_return(p):
    '''return : RETURN expr'''
    p[0] = Node('return', [p[2]])

def p_main(p):
    '''main : MAIN OPENPAR CLOSEPAR block'''
    p[0] = Node('main', [p[4]])
    
parser = yacc.yacc()

def build_tree(code):
    return parser.parse(code)

def do_tests(n):
    for i in range (1, n + 1):
        fin = open('test'+ str(i)+'.txt', 'r')
        sys.stdout = open('test'+str(i) + '.out', 'w')
        result = build_tree(fin.read())
        fin.close()
        print(result)

def main():
    do_tests(6)
    #fin = open(sys.argv[1], 'r')
    #sys.stdout = open(sys.argv[1] + '.out', 'w')
    #result = build_tree(fin.read())
    #fin.close()
    #print(result)

main()
