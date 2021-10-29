import ply.yacc as yacc
from lex import tokens
from lex import lexer
from lex import colored
from lex import ERROR
from lex import do_lex
import sys


class Node:
    def __init__(self, value: str, children: list):
        self.value = value
        self.children = children

    def get_val(self):
        res = ""
        for i in range(len(self.children)):
            res = res + " " + self.children[i].value
        return res


def bfs(v: Node):
    q = [v]
    i = 0
    while len(q) > i:
        cur = q[i]
        i += 1
        print(colored("Node:", "yellow"), colored(cur.value, "green"), end=": ")
        print(colored("Children", "blue"), end=" ")
        if len(cur.children) == 0:
            print(colored("EMPTY", "cyan"), end=" ")

        for j in cur.children:
            print(colored(j.value, "magenta"), end=" | ")
            q.append(j)
        print()


def p_grammar(p):
    'grammar : rule_list'
    p[0] = p[1]


def p_rule_list(p):
    '''rule_list :
                    | rule_list rule
                    | rule_list comment
                    | rule'''
    if len(p) == 2:
        p[0] = Node("", [p[1]])
    else:
        p[0] = Node("", [p[1], p[2]])

    p[0].value = p[0].get_val()


def p_comment(p):
    '''comment : MULTILINE_COMMENT'''
    p[0] = Node(p[1], [])


def p_rule(p):
    'rule : RULENAME EQ expression1'
    p[0] = Node('', [Node(p[1], []), Node(p[2], []), p[3]])
    p[0].value = p[0].get_val()

def p_expression1(p):
    '''expression1 :
                    | expression1 COMMA expression2
                    | expression1 COMMA INDENT expression2
                    | expression2'''
    if len(p) == 2:
        p[0] = Node("", [p[1]])
    elif len(p) == 4:
        p[0] = Node("", [p[1], Node(p[2], []), p[3]])
    else:
        p[0] = Node("", [p[1], Node(p[2], []), p[4]])
    p[0].value = p[0].get_val()

def p_expression2(p):
    '''expression2 :
                    | expression2 ALT expression3
                    | expression2 ALT INDENT expression3
                    | expression3'''
    if len(p) == 2:
        p[0] = Node("", [p[1]])
    elif len(p) == 4:
        p[0] = Node("", [p[1], Node(p[2], []), p[3]])
    else:
        p[0] = Node("", [p[1], Node(p[2], []), p[4]])
    p[0].value = p[0].get_val()

def p_expression3(p):
    '''expression3 :
                    | LPAREN expression1 RPAREN
                    | LBRACE expression1 RBRACE
                    | LBRACKET expression1 RBRACKET
                    | RULENAME
                    | PLAINTEXT'''
    if len(p) == 2 and p[1]:
        p[0] = Node(p[1], [])
    elif p[1] == '(' or p[1] == '[' or p[1] == '{':
        p[0] = Node('', [Node(p[1], []), p[2], Node(p[3], [])])
        p[0].value = p[0].get_val()
    elif len(p) == 5:
        p[0] = Node('', [p[1], Node(p[2], []), p[4]])
        p[0].value = p[0].get_val()
    else:
        assert False


def p_error(p):
    print("Syntax error")


parser = yacc.yacc()


def input_and_parse():
    try:
        with open(input("enter path to file you want to parse"), 'r') as f:
            s = f.read()
            filename_out = input("now enter filename to lexer result or leave empty to default")
            do_lex(s, filename_out)
    except:
        print(colored("Unable to open file", "red"))
        input_and_parse()
        return True
    try:
        res_grammar = parser.parse(s)
    except:
        return False

    bfs(res_grammar)
    return True


response = input_and_parse()
if not response:
    print(colored("Incorrect grammar", "red"))
    exit(1)