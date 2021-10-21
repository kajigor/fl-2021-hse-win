import ply.yacc as yacc
import sys
from lex import tokens

class Tree:
  nodes = []
  adj = {}
  def dfs(x):
    print("Node", x, ":", Tree.nodes[x])
    if (len(Tree.adj[x]) > 0):
      print("Edges to nodes", Tree.adj[x])
    print("")
    for child in Tree.adj[x]:
      Tree.dfs(child)


precedence = (
    ('right', 'AND', 'OR'),
    ('nonassoc', 'NOT'),
    ('nonassoc', 'EQUAL', 'NOTEQUAL', 'LESSEQUAL', 'GREATEQUAL', 'LESS', 'GREAT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
    ('right', 'CARET')
)

def p_error(p):
  print("Parse error", p)
  exit()

def p_code(p):
  '''code : list_declarations VOID MAIN BRACKET_OPEN BRACKET_CLOSE body
          | VOID MAIN BRACKET_OPEN BRACKET_CLOSE body'''
  Tree.nodes.append("Initial node")
  p[0] = len(Tree.nodes) - 1
  if (len(p) == 7):
    Tree.nodes.append("main")
    p[3] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[1], p[3]]
    Tree.adj[p[3]] = [p[6]]
  else:
    Tree.nodes.append("main")
    p[2] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[2]]
    Tree.adj[p[2]] = [p[5]]

def p_list_declarations(p):
  '''list_declarations : list_declarations declaration
                       | declaration'''
  if (len(p) == 2):
    Tree.nodes.append("function declaration block")
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[1]]
  else:
    Tree.nodes.append("function declaration block")
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = Tree.adj[p[1]]
    Tree.adj[p[0]].append(p[2])


def p_function_declaration(p):
  '''declaration : VOID FUNCTION_NAME BRACKET_OPEN BRACKET_CLOSE body
                 | VOID FUNCTION_NAME BRACKET_OPEN list_args BRACKET_CLOSE body'''
  if (len(p) == 6):
    Tree.nodes.append("declaration function " + p[2])
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[5]]
  else:
    Tree.nodes.append("declaration function " + p[2])
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[4], p[6]]

def p_body(p):
  '''body : BEGIN return_operator END
          | BEGIN operator return_operator END'''
  Tree.nodes.append("function body")
  p[0] = len(Tree.nodes) - 1
  if (len(p) == 4):
    Tree.adj[p[0]] = [p[2]]
  else:
    Tree.adj[p[0]] = [p[2], p[3]]

def p_return_operator(p):
  '''return_operator : RETURN expr SEMICOLON'''
  Tree.nodes.append("return operator")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = [p[2]]

def p_skip(p):
  '''expr : SKIP'''
  Tree.nodes.append("skip")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = []  

def p_assigment(p):
    '''operator : VARIABLE ASSIGNMENT expr'''
    Tree.nodes.append(p[1])
    p[1] = len(Tree.nodes) - 1
    Tree.adj[p[1]] = []
    Tree.nodes.append(p[0])
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[1], p[3]]

def p_if(p):
  '''operator : IF BRACKET_OPEN expr BRACKET_CLOSE BEGIN expr END'''
  Tree.nodes.append("if statement")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = [p[3], p[6]]

def p_if_else(p):
  '''operator : IF BRACKET_OPEN expr BRACKET_CLOSE BEGIN expr END ELSE BEGIN expr END'''
  Tree.nodes.append("if else statement")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = [p[3], p[6], p[10]]

def p_while(p):
  '''operator : WHILE BRACKET_OPEN expr BRACKET_CLOSE BEGIN expr END'''
  Tree.nodes.append("while statement")
  p[0] = len(Tree.nodes) - 1 
  Tree.adj[p[0]] = [p[3], p[6]]

def p_function_call_expr(p):
  '''expr : FUNCTION_NAME BRACKET_OPEN BRACKET_CLOSE
          | FUNCTION_NAME BRACKET_OPEN list_args BRACKET_CLOSE'''
  Tree.nodes.append("function call")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = []
  if (len(p) == 5):
    Tree.adj[p[0]].append(p[3])

def p_function_call_operator(p):
  '''operator : FUNCTION_NAME BRACKET_OPEN BRACKET_CLOSE
              | FUNCTION_NAME BRACKET_OPEN list_args BRACKET_CLOSE'''
  Tree.nodes.append("function call")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = []
  if (len(p) == 5):
    Tree.adj[p[0]].append(p[3])

def p_list_operators(p):
  '''operator : operator SEMICOLON operator
              | operator SEMICOLON'''
  Tree.nodes.append("Sequence")
  p[0] = len(Tree.nodes) - 1
  if (len(p) == 3):
    Tree.adj[p[0]] = [p[1]]
  else:
    Tree.adj[p[0]] = [p[1], p[3]]

def p_list_args(p):
  '''list_args : list_args COMMA VARIABLE
               | VARIABLE'''
  if (len(p) == 2):
    Tree.nodes.append(p[1])
    p[1] = len(Tree.nodes) - 1
    Tree.adj[p[1]] = []
    Tree.nodes.append("list args")
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = [p[1]]
  else:
    Tree.nodes.append(p[3])
    p[3] = len(Tree.nodes) - 1
    Tree.adj[p[3]] = []
    Tree.nodes.append("list args")
    Tree.adj[p[0]] = Tree.adj[p[1]]
    Tree.adj[p[0]].append(p[3])

def p_brackets(p):
  '''expr : BRACKET_OPEN expr BRACKET_CLOSE'''
  Tree.nodes.append("brackets")
  p[0] = len(Tree.nodes) - 1
  Tree.adj[p[0]] = [p[2]]


def p_number(p):
    'expr : NUMBER'
    Tree.nodes.append(int(p[1]))
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = []

def p_string(p):
    'expr : STRING'
    Tree.nodes.append(p[1])
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = []

def p_variable(p):
    'expr : VARIABLE'
    Tree.nodes.append(p[1])
    p[0] = len(Tree.nodes) - 1
    Tree.adj[p[0]] = []

def p_exprs(p):
    '''expr : expr CARET expr
            | MINUS expr
            | expr MULT expr
            | expr DIV expr
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
    if (len(p) == 4):
      Tree.nodes.append(p[2])
      p[0] = len(Tree.nodes) - 1
      Tree.adj[p[0]] = [p[1], p[3]]
    else:
      Tree.nodes.append(p[1])
      p[0] = len(Tree.nodes) - 1
      Tree.adj[p[0]] = [p[2]]

def main():
  fin = open(sys.argv[1], 'r')
  sys.stdout = open(sys.argv[1] + '.out', 'w')
  parser = yacc.yacc()
  result = parser.parse(fin.read())
  fin.close()
  print("Nodes:", Tree.nodes)
  print("Adjacency list:", Tree.adj)

  Tree.dfs(result)
main()