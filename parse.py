import ply.yacc as yacc
import sys
from lex import tokens
import networkx as nx
import matplotlib.pyplot as plt


import pydot

class Node:
    def __init__(self, my_operation, my_kids):
        self.operation = my_operation
        self.kids = my_kids

class Result:
    def __init__(self):
        self.start_nonterm = []
        self.current_id = 0
        self.nodes = []
        self.graph = pydot.Dot("my_graph", graph_type="graph")
        self.graph.obj_dict['attributes']["size"] = '"10,10!"'
        self.graph.obj_dict['attributes']["dpi"] = "144"
        self.num_of_nodes = 0
    def build_tree(self, a):
        my_i = self.num_of_nodes
        self.graph.add_node(pydot.Node(str(my_i), label=a.operation))
        for element in a.kids:
            self.num_of_nodes += 1
            self.graph.add_edge(pydot.Edge(str(my_i), str(self.num_of_nodes)))
            self.build_tree(element)


def p_lang(p):
    '''Language : Rule
                | Start_nonterm '''

def p_rule(p):
    ''' Rule : ID EQUALITY Expr '''
    parser.my_result.nodes.append(Node("ID is " + p[1], [p[3]]))

def p_start(p):
    ''' Start_nonterm : START EQUALITY ID '''
    parser.my_result.start_nonterm.append(p[3])

def p_expr_symbol(p):
    ''' Expr : SYMBOL '''
    p[0] = Node("Symbol - " + p[1], [])

def p_expr_arg(p):
    ''' Expr : ID
             | L_BRACKETS Expr R_BRACKETS
             | Expr MULT
    '''
    if len(p) == 2:
        p[0] = Node("ID - " + p[1], [])
    elif len(p) == 3:
        p[0] = Node("*", [p[1]])
    elif len(p) == 4:
        p[0] = Node("()", [p[2]])

def p_sqr_brkts(p):
    ''' Expr : L_SQUARE Expr R_SQUARE '''
    p[0] = Node("[]", [p[2]])

def p_expr_args_plus(p):
    ''' Expr : Expr PLUS Expr '''
    p[0] = Node("+", [p[1], p[3]])

def p_expr_args_alt(p):
    ''' Expr : Expr ALT Expr '''
    p[0] = Node("|", [p[1], p[3]])

def p_error(p):
    raise Exception("Syntax error")

parser = yacc.yacc()

parser.my_result = Result()
parser.is_ok = True

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')


while True:
    try:
        s = input()
    except EOFError:
        break
    if not s:
        continue
    try:
        result = parser.parse(s)
    except Exception as e:
        print("Error: " + str(e))
        parser.is_ok = False
        break

if parser.is_ok:
    print("Non terminal is " + parser.my_result.start_nonterm[0])
    parser.my_result.build_tree(parser.my_result.nodes[0])
    my_networkx_graph = nx.drawing.nx_pydot.from_pydot( parser.my_result.graph)
    nx.draw(my_networkx_graph)
    plt.show()