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
        self.to_ = []
        self.from_ = []
class Automaton:
  def __init__(self):           
    self.alphabet =[]
    self.edges = []
    self.states = []   
    self.term_states = []      
    self.index_edges = {}
    self.index_states = {}
    self.edges_to = []
    self.in_alph ={}
    start =""
  def state_eq(self):
    for i in self.states:
      for j in self.states:
        if i.is_terminal == j.is_terminal and i.is_start == j.is_start \
          and i.is_stock == j.is_stock and i!=j and\
          sorted(i.to_) == sorted(j.to_) and sorted(i.from_) == sorted(j.from_):
          print('\n'+(str)(i.name) + ' and ' + (str)(j.name) + ' are equal!')
    print("\nAll states are unique!")

  def symbols_unique(self):
    return len(set(self.alphabet))==len(self.alphabet)

  def is_determ(self):
    flag = True
    for i in self.states:
      symb = {}
      for j in i.to_:
        a, b = j
        if b in symb:
          flag = False
        else:
          symb[b] = 1  
    return flag 

  def is_full(self):
    flag = True
    for i in self.states:
      all_simb = []
      for j in i.to_:
        a, b = j
        all_simb.append(b)
      if(len(set(all_simb)) != len(self.alphabet)):
        flag = False 
    return flag 

  def print_automato(self):
      for i in self.term_states:
        if(not i in self.index_states):
          raise Exception("Terminal state "+ "'"+(str)(i)+"'"+" is out of State set!")
      if(not self.start in self.index_states):
         raise Exception("Start state "+"'"+(str)(self.start)+"'"+" is out of State set!") 
      if(self.is_determ()):
        print("Automaton is deterministic!")
      else:
        print("Automaton is not deterministic!")  
      if(self.is_full()):
        print("Automaton is full!") 
      else: 
        print("Automaton is not full!")  
      print("\nStates:") 
      start = -1         
      for i in self.states:
            print(i.name, end=": ")
            if(i.is_terminal):
              print("terminal")
            elif(i.is_start):
              print("start")
              start = i.name
            elif(i.is_stock):
              print("stock")
            else:
              print("normal") 
      print("\nEdges:\n")          
      for i in self.edges:
            print("from ", end="")
            print(i.state_from, end="")
            print(" to ", end="")
            print(i.state_to, end=". ")
            print("Symbols: ", end=' ')
            print(i.symbols)
      if start!=-1:
        print("\nAutomaton has a start state!\n")
      else:
        print("Automaton does not have a start state!\n")       
      if(self.symbols_unique()):
        print("Symbols in alphabet are unique!")
      else:
        print("Symbols in alphabet are not unique!")   
      self.state_eq()  
def p_automaton(p):
      '''Automaton : start_state
                    | States
                    | term_state
                    | Alphabet
                    | edges 
                    '''               
def p_start_state(p):
  'start_state : START ARROW NUM' 
  parser.automaton.start = p[3]

def p_empty(p):
    'empty :'
    pass    
def p_term_state(p):
  '''term_state : TERM COLON OPEN_BRACKET NUM term_state_list CLOSE_BRACKET
                 | TERM COLON OPEN_BRACKET empty CLOSE_BRACKET'''
  if p[5]!=")":              
    parser.automaton.term_states.append(p[4])

def p_term_state_list(p):
  '''term_state_list : COMMA NUM term_state_list  
                    | empty'''
  if p[1]==',':                  
    parser.automaton.term_states.append(p[2]) 

def p_states(p):
  '''States : STATES COLON OPEN_BRACKET NUM states_list CLOSE_BRACKET
             | STATES COLON OPEN_BRACKET empty CLOSE_BRACKET'''
  if p[5]!=")":
    if(not (str)(p[4]).isdigit()):
      raise Exception("State "+"'"+(str)(p[4])+"'"+ +" is not a digit!")           
    current_state=State(p[4])
    if parser.automaton.start== current_state.name:
      current_state.is_start = True
    for i in parser.automaton.term_states:
      if i == current_state.name:
        current_state.is_terminal = True
    parser.automaton.states.append(current_state)
    parser.automaton.index_states[p[4]] = len(parser.automaton.states) -1

  
def p_states_list(p):
  '''states_list : COMMA NUM states_list
                  | empty'''
  if p[1]==",":
    if(not (str)(p[2]).isdigit()):
        raise Exception("State "+"'"+(str)(p[2])+"'"+ +" is not a digit!")                 
    current_state=State(p[2])
    if parser.automaton.start == current_state.name:
      current_state.is_start = True
    for i in parser.automaton.term_states:
      if i == current_state.name:
        current_state.is_terminal = True
    parser.automaton.states.append(current_state)
    parser.automaton.index_states[p[2]] = len(parser.automaton.states) -1
  
def p_alphabet(p):
    '''Alphabet : ALPHABET COLON OPEN_BRACKET WORD Words CLOSE_BRACKET
                 | ALPHABET COLON OPEN_BRACKET empty CLOSE_BRACKET'''
    if len(p) > 6:             
      parser.automaton.alphabet.append(p[4])
      parser.automaton.in_alph[p[4]] = 1

def p_words(p):
    '''Words : COMMA WORD Words
              | empty'''
    if p[1]==",":          
      parser.automaton.alphabet.append(p[2])
      parser.automaton.in_alph[p[2]] = 1

def p_edges(p):
  '''edges : LIST COLON VERTEX_FROM OPEN_BRACKET VERTEX_TO WORD CLOSE_BRACKET edge_list
          | VERTEX_FROM OPEN_BRACKET VERTEX_TO WORD CLOSE_BRACKET edge_list
          | VERTEX_FROM empty'''
  if(len(p)>3): 
    if(len(p)>7):
      i_from = 3
      i_to = 5
      i_word=6
    else:
      i_from = 1
      i_to = 3
      i_word=4  
    parser.automaton.edges_to.append((p[i_to], p[i_word]))
    if(not p[i_from].isdigit()):
          raise Exception("State "+"'"+(str)(p[i_from])+"'"+ +" is not a digit!")
    for pair in parser.automaton.edges_to:
        
        parser.automaton.states[parser.automaton.index_states[(int)(p[i_from])]].to_.append(pair)
        a, b = pair
        if(not a.isdigit()):
          raise Exception("State "+"'"+(str)(a)+"'" +" is not a digit!")
        if(not b in parser.automaton.in_alph):
          raise Exception("Word "+"'"+(str)(b)+"'"+" is not in alphabet!")
        parser.automaton.states[parser.automaton.index_states[(int)(a)]].from_.append((p[i_from], b))
        pair2=(p[i_from], a)
        if pair2 in parser.automaton.index_edges:
          parser.automaton.edges[parser.automaton.index_edges[pair2]].symbols.append(p[i_word])
        else:
          edge = Edge()
          edge.add_to(a)
          edge.add_from(p[i_from])
          edge.symbols.append(b)
          parser.automaton.edges.append(edge) 
          parser.automaton.index_edges[pair2] = len(parser.automaton.edges)-1 
    parser.automaton.edges_to.clear()

def p_edge_list(p):
    '''edge_list : VERTICAL_LINE OPEN_BRACKET VERTEX_TO WORD CLOSE_BRACKET edge_list
                  | empty'''
    if p[1] == "|":              
      parser.automaton.edges_to.append((p[3], p[4]))
    
def p_error(p):
  raise Exception("Syntax error. Look at the format requirements!")

parser = yacc.yacc()
parser.automaton=Automaton()
parser.is_nice_auto = True
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
    result=parser.parse(s)
  except Exception as e:
    print("some errors during parsing occurred >>> "+(str)(s)+"\n"+"Invalid automaton: "+(str)(e))
    parser.is_nice_auto=False
    break  
if(parser.is_nice_auto):
  try:
    parser.automaton.print_automato()
  except Exception as e:
    print("Invalid automaton: "+(str)(e))  