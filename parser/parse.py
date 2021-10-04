import ply.yacc as yacc
import sys
from lex import tokens

class Edge:
    def __init__(self):
        self.state_from = ""
        self.state_to = ""
        self.symbols = []
        
    def add_from(self, from_):
        if self.state_from != "":
            raise Exception("Vertex from has already appeared!")
        self.state_from = from_
        
    def add_to(self, to):
        if self.state_to != "":
            raise Exception("Vertex to has already appeared!")
        self.state_to = to
        
class State:
    def __init__(self, name_):
        self.name = name_
        self.is_terminal = False
        self.is_start = False
        self.is_stock = False
        self.out_edge = []
        self.in_edge = []
         
alphabet =[]
edges = []
states = []   
term_states = []      
count_strings = 0
start = []
index_edges = {}
def print_automato():
     print("States:\n")            
     for i in states:
          print("q", end="")
          print(i, end=": ")
          if(i.is_terminal):
            print("terminal")
          elif(i.is_start):
            print("start")
          elif(i.is_stock):
            print("stock")
          else:
            print("normal") 
     print("\nEdges\n")          
     for i in edges:
          print("from q", end="")
          print(i.state_from, end="")
          print(" to ", end="")
          print("q", end="")
          print(i.state_to, end=". ")
          print("Symbols: ")
          print(i.symbols)
               
def p_automaton(p):
      '''Automaton : start_state
                    | term_state
                    | States
                    | Alphabet
                    | edges 
                    '''
def p_start_state(p):
  'start_state: START ARROW NUM'
  start.append(p[0])

def p_term_state(p):
  'term_state: TERM COLON OPEN_BRACKET NUM term_state_list CLOSE_BRACKET'
  term_states.append(4)


def p_term_state_list(p):
  'term_state_list: COMMA NUM term_state_list'
  term_states.append(2) 


def p_states(p):
  'States: STATES COLON OPEN_BRACKET NUM states_list CLOSE_BRACKET'
  current_state=State(p[4])
  for i in start:
    if i== current_state.name:
      current_state.is_start = True
  for i in term_states:
    if i == current_state.name:
      current_state.is_terminal = True
  states.append(current_state)
  
def p_states_list(p):
  'states_list: COMMA NUM states_list' 
  current_state=State(p[2])
  if start == current_state.name:
    current_state.is_start = True
  for i in term_states:
    if i == current_state.name:
      current_state.is_terminal = True
  states.append(current_state)
  
def p_alphabet(p):
    'Alphabet: ALPHABET OPEN_BRACKET WORD Words CLOSE_BRACKET'
    parser.object = "alphabet"
    alphabet.append(p[3])
def p_words(p):
    'Words: COMMA WORD Words'
    alphabet.append(p[2])  

def p_start_list(p):
    'start_list: LIST COLON'
    parser.object = "list"


def p_edges(p):
  'edges: VERTEX_FROM COLON OPEN_BRACKET VERTEX_TO POINT_COMMA WORD CLOSE_BRACKET edge_list'
  parser.vertex_from = p[1]
  pair = (p[1], p[4])
  if pair in index_edges:
    edges[index_edges[pair]].symbols.append(p[6])
  else:
    edge = Edge()
    edge.add_state_to(p[4])
    edge.add_state_from(p[1])
    edge.symbols.append(p[6])
    edges.append(edge) 
    index_edges[pair] = len(edges)-1   


def p_edge_list(p):
    'edge_list: VERTICAL_LINE OPEN_BRACKET VERTEX_TO POINT_COMMA WORD CLOSE_BRACKET'
    pair = (parser.vertex_from, p[3])

    if pair in index_edges:
      edges[index_edges[pair]].symbols.append(p[5])

    else:
      edge = Edge()
      edge.add_state_to(p[3])
      edge.add_state_from(parser.vertex_from)
      edge.symbols.append(p[5])
      edges.append(edge)    
      index_edges[pair] = len(edges)-1

def p_error(p):
  print("Syntax error")

parser = yacc.yacc()
parser.vertex_from = 0
sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')
while True:
  try:
    s = input()
  except EOFError:
    break
  if not s:
    continue
  result=parser.parse(s)
print_automato()  