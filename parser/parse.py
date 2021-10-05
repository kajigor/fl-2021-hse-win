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
index_edges = {}
edges_to = []
def print_automato():
     print("\nStates:")            
     for i in states:
          print(i.name, end=": ")
          if(i.is_terminal):
            print("terminal")
          elif(i.is_start):
            print("start")
          elif(i.is_stock):
            print("stock")
          else:
            print("normal") 
     print("\nEdges:\n")          
     for i in edges:
          print("from ", end="")
          print(i.state_from, end="")
          print(" to ", end="")
          print(i.state_to, end=". ")
          print("Symbols: ", end=' ')
          print(i.symbols)
               
def p_automaton(p):
      '''Automaton : start_state
                    | States
                    | term_state
                    | Alphabet
                    | edges 
                    '''               
def p_start_state(p):
  'start_state : START ARROW NUM'
  global start 
  start = p[3]

def p_empty(p):
    'empty :'
    pass    
def p_term_state(p):
  '''term_state : TERM COLON OPEN_BRACKET NUM term_state_list CLOSE_BRACKET
                 | TERM COLON OPEN_BRACKET empty CLOSE_BRACKET'''
  if p[5]!=")":              
    term_states.append(p[4])

def p_term_state_list(p):
  '''term_state_list : COMMA NUM term_state_list  
                    | empty'''
  if p[1]==',':                  
    term_states.append(p[2]) 

def p_states(p):
  '''States : STATES COLON OPEN_BRACKET NUM states_list CLOSE_BRACKET
             | STATES COLON OPEN_BRACKET empty CLOSE_BRACKET'''
  if p[5]!=")":           
    current_state=State(p[4])
    if start== current_state.name:
      current_state.is_start = True
    for i in term_states:
      if i == current_state.name:
        current_state.is_terminal = True
    states.append(current_state)

  
def p_states_list(p):
  '''states_list : COMMA NUM states_list
                  | empty'''
  if p[1]==",":                 
    current_state=State(p[2])
    if start == current_state.name:
      current_state.is_start = True
    for i in term_states:
      if i == current_state.name:
        current_state.is_terminal = True
    states.append(current_state)
  
def p_alphabet(p):
    '''Alphabet : ALPHABET COLON OPEN_BRACKET WORD Words CLOSE_BRACKET
                 | ALPHABET COLON OPEN_BRACKET empty CLOSE_BRACKET'''
    if len(p) > 6:             
      alphabet.append(p[4])

def p_words(p):
    '''Words : COMMA WORD Words
              | empty'''
    if p[1]==",":          
      alphabet.append(p[2])

def p_edges(p):
  '''edges : VERTEX_FROM OPEN_BRACKET VERTEX_TO WORD CLOSE_BRACKET edge_list
          | VERTEX_FROM empty'''
  if(len(p)>3): 
    edges_to.append((p[3], p[4]))   
    for pair in edges_to:
        a, b = pair
        pair2=(p[1], a)
        if pair2 in index_edges:
          edges[index_edges[pair2]].symbols.append(p[4])
        else:
          edge = Edge()
          edge.add_to(a)
          edge.add_from(p[1])
          edge.symbols.append(b)
          edges.append(edge) 
          index_edges[pair2] = len(edges)-1 
    edges_to.clear()

def p_edge_list(p):
    '''edge_list : VERTICAL_LINE OPEN_BRACKET VERTEX_TO WORD CLOSE_BRACKET edge_list
                  | empty'''
    if p[1] == "|":              
      edges_to.append((p[3], p[4]))
    
def p_error(p):
  print("Syntax error")

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
  result=parser.parse(s)
print_automato()