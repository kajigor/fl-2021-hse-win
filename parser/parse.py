from typing import Counter
import ply.yacc as yacc

from lex import tokens

# if 42 then (if 0 then 777 else 9)
class Edge:
    def __init__(self):
        self.state_from = ""
        self.state_to = ""
        self.symbols = []
        
    def add_symbol(self, symbol):
        self.symbols.append(symbol)
        
    def add_state_from(self, state_from_):
        if self.state_from != "":
            raise Exception("This edge already has an outgoing state")
        self.state_from = state_from_
        
    def add_state_to(self, state_to_):
        if self.state_to != "":
            raise Exception("This edge already has an incoming state")
        self.state_to = state_to_
        
class State:
    def __init__(self, name_):
        self.name = name_
        self.is_terminal = False
        self.is_start = False
        self.is_stock = False
        self.out_edge = []
        self.in_edge = []
         
    def change_terminality(self):
        self.terminality = True

    def equality_state(state1, state2):
        if state1.terminality != state2.terminality:
            return False
        if state1.from_state != state2.from_state:
            return False
        if state1.to_state != state2.to_state:
            return False
        return True  
alphabet =[]
edges = []
states = []         
count_strings = 0
def print_automato():
     for j in states:
            for i in alphabet:
                fl = 0
                for l in j.out_edge:
                    if i in l.symbols:
                        fl += 1
                if fl == 0:
                  raise Exception("The automaton is not complete")
                if fl > 1:
                  raise Exception("The automaton is not deterministic")
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
     is_complete = True
     for i in edges:
          print("from q", end="")
          print(i.state_from, end="")
          print(" to ", end="")
          print("q", end="")
          print(i.state_to, end=". ")
          print("Symbols: ")
          print(i.symbols)
               
def p_automaton(p):
      '''Automaton : Alphabet
                    | States
                    | Terminal
                    | Edges '''
def p_alphabet(p):
    'Alphabet: OPEN_BRACKET Words VERTICAL_LINE'
    parser.object = "alphabet"
    parser.is_positive_balance = True

def p_words(p):
    'Words: COMMA WORD Words'
    alphabet.append(p[2])  

def p_edges(p):
    'Edges: VERTICAL_LINE edge_list VERTICAL_LINE'
    states.append(count_strings)
    count_strings=count_strings + 1
    counter = 0
    for i in p[2]:
      edge = Edge()
      edge.add_state_from = count_strings
      edge.add_state_to = i
      edge.symbols.append(alphabet)
      edges.append()

def p_edge_list(p):
    'edge_list: NUM COMMA edge_list'    
def p_error(p):
  print("Syntax error")

parser = yacc.yacc()

while True:
  try:
    s = input("calc> ")
  except EOFError:
    break
  if not s:
    continue
  result=parser.parse(s)
  print(result)






