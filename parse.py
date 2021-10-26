import ply.yacc as yacc
import sys
from lex import tokens

import graphviz

graph = graphviz.Graph()
nodes = 0
definitions = []
programs = []

class Node:
    def __init__(self, label_, kids_):
        self.label = label_
        self.kids = kids_
        self.ind = nodes

def add(node):
    global nodes
    graph.node(str(nodes), node.label)
    nodes += 1
    for kid in node.kids:
        graph.edge(str(node.ind), str(kid.ind))

def check_goals():
    return len(programs) == 1

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQ')
)

def p_program_def(p):
    '''program : define
               | COMMENT '''

def p_program_goal(p):
    ''' program : goal'''
    p[0] = Node("Program", [p[1]] + definitions)
    add(p[0])
    programs.append(p[0])

def p_define(p):
    '''define : DEFINE FUNCTION DO goal FOR args'''
    p[0] = Node("Def: " + p[2][1:], [p[4]] + p[6])
    definitions.append(p[0])
    add(p[0])

def p_goal_and(p):
    ''' goal : goal AND goal '''
    p[0] = Node("Operator: *", [p[1], p[3]])
    add(p[0])

def p_goal_or(p):
    ''' goal : goal OR goal '''
    p[0] = Node("Operator: +", [p[1], p[3]])
    add(p[0])

def p_goal_eq(p):
    ''' goal : atom EQ atom '''
    p[0] = Node("Operator: ?=", [p[1], p[3]])
    add(p[0])

def p_factor(p):
    ''' factor : LBR goal RBR '''
    p[0] = p[2]

def p_goal_br(p):
    ''' goal : factor '''
    p[0] = p[1]

def p_goal_call(p):
    ''' goal : DO FUNCTION FOR args
             | DO FUNCTION '''
    if len(p) == 3:
        p[0] = Node("Call: " + p[2][1:], [])
    if len(p) == 5:
        p[0] = Node("Call: " + p[2][1:], p[4])
    add(p[0])

def p_atom(p):
    '''atom : VARIABLE
            | LBR MAKE CONSTRUCTOR RBR
            | LBR MAKE CONSTRUCTOR FROM args RBR'''
    if len(p) == 2:
        p[0] = Node("Var: " + p[1], [])
    if len(p) == 5:
        p[0] = Node("Constructor: " + p[3][1:], [])
    if len(p) == 7:
        p[0] = Node("Constructor: " + p[3][1:], p[5])
    add(p[0])

def p_args(p):
    ''' args : atom
             | atom args '''
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = [p[1]] + p[2]

def p_error(p):
    raise Exception("Syntax error at symbol ", p)


parser = yacc.yacc()

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
    break

if (check_goals()):
    try:
        graph.render(sys.argv[1] + ".graph")
    except Exception as e:
        print("Error: " + str(e))
else:
    print("Error: too many goals, you can write a lot of definitions but only one goal for your program")
