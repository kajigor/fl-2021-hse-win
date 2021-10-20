import ply.yacc as yacc
from lex import tokens
from lex import lexer
import sys

class Node:
    def __init__(self, value: str, children: list):
        self.value = value
        self.children = children

    def get_val(self):
        res = ""
        for i in range (len(self.children)):
            res = res + " " + self.children[i].value
        return res

def bfs(v :Node):
    q = [v]
    i = 0
    while len(q) > i:
        cur = q[i]
        i += 1
        print(cur.value, end = ": ")
        for j in cur.children:
            print(j.value, end = " @ ")
            q.append(j)
        print()




def p_grammar(p):
    'grammar : rule_list'
    p[0] = p[1]


def p_rule_list(p):
    '''rule_list :
                    | rule_list rule
                    | rule'''
    if len(p) == 2:
        p[0] = Node("", [p[1]])
    else:
        p[0] = Node("", [p[1], p[2]])

    p[0].value = p[0].get_val()


def p_rule(p):
    'rule : RULENAME EQ expression'
    p[0] = Node('', [Node(p[1], []), Node(p[2], []), p[3]])
    p[0].value = p[0].get_val()


def p_expression(p):
    '''expression :
                    | expression COMMA expression
                    | expression ALT expression
                    | expression COMMA INDENT expression
                    | expression ALT INDENT expression
                    | LPAREN expression RPAREN
                    | LBRACE expression RBRACE
                    | LBRACKET expression RBRACKET
                    | RULENAME
                    | PLAINTEXT'''
    if len(p) == 2:
        p[0] = Node(p[1], [])
    elif p[1] == '(' or p[1] == '[' or p[1] == '{':
        p[0] = Node('', [Node(p[1], []), p[2], Node(p[3], [])])
        p[0].value = p[0].get_val()
    elif len(p) == 5:
        p[0] = Node('', [p[1], Node(p[2], []), p[4]])
        p[0].value = p[0].get_val()
    elif p[2] == ',' or p[2] == '|':
        p[0] = Node('', [p[1], Node(p[2], []), p[3]])
        p[0].value = p[0].get_val()
    else:
        assert False

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

# try:
s = ''.join(open(sys.argv[1]).readlines())
res_grammar = parser.parse(s)
# except:
#     print("Unable to open file")
#     exit(1)
bfs(res_grammar)