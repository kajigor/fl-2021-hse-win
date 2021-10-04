import ply.yacc as yacc
from lex import tokens
import sys

# автомат -- граф, характеризуется состояними (вершины State) и ребрами перехода (ребра Edges)

class State:
  def __init__(self, number_):
    self.number = number_
    self.symbols = []
    self.is_terminal = 0
    self.in_edges = []
    self.out_edges = []

  def add_symbol(self, symbol):
    self.symbols.append(symbol)

  def make_terminal(self):
    self.is_terminal = 1

  def add_in_edge(self, edge):
    self.in_edge.append(edge)

  def add_out_edge(self, edge):
    self.out_edges.append(edge)        

class Edge:
  def __init__(self):
    self.from_state = 0
    self.to_state = 0
    self.symbols = []

  def init_from_state(self, state_number):
    self.from_state = state_number

  def init_to_state(self, state_number):
    self.to_state = state_number    

  def add_symbol(self, symbol):
    self.symbols.append(symbol)      

class Automat:
  def __init__(self):
    self.alphabet_size = 0
    self.alphabet = []
    self.count_states = 0
    self.start_state = 0
    self.count_terminal = 0
    self.terminal_states = []
    #self.count_edges = 0
    self.edges = []

  def init_alphabet_size(self, size):
    self.alphabet_size = size

  def add_alphabet_symbol(self, symbol):
    self.alphabet.append(symbol)

  def init_count_states(self, count):
    self.count_states = count

  def init_start_state(self, state):
    self.start_state = state

  def init_count_terminal(self, count):
    self.count_terminal = count

  def add_terminal_state(self, state_number):
    self.terminal_states.append(state_number)

  #def init_count_edges(self, count):
    #self.count_edges = count

  def add_edge(self, edge):
    self.edges.append(edge)  

  def print_automat(self):
    self.alphabet.sort()
    print("Alphabet:  ", end="")
    print("(", end = "")
    print(', '.join(self.alphabet), end = "")
    print(")")

    print("Start:      ", end="")
    print(self.start_state)

    self.terminal_states.sort()
    sarr = [str(a) for a in self.terminal_states]
    print("Terminals:  ", end="")
    print(', '.join(sarr))

    print("Edges:    ")
    for edge in self.edges:
      print("            ", end = "")
      print(edge.from_state, end = "")
      print(" --> ", end = "")
      print(edge.to_state, end = "")
      edge.symbols.sort()
      print(" (", end = "")
      print(', '.join(edge.symbols), end = "")
      print(")")

automat = Automat()
current_edge = Edge()      

def p_automaton(p):
  '''Automat : Alphabet
               | States_count
               | Start_state
               | Terminals
               | Edges '''

def p_alphabet(p):
  'Alphabet : ALPHABET COLON NUM DASH OPARENTHESES str_alphabet_symbols CPARENTHESES'

def p_states_count(p):
  'States_count : Q COLON NUM'
  automat.init_count_states(p[3])

def p_start_state(p):
  'Start_state : START COLON NUM'
  automat.init_start_state(p[3])

def p_terminals(p):
  'Terminals : T COLON NUM DASH str_terminal_nums'

def p_edges(p):
  'Edges : EDGES COLON str_edges'

def p_str_alphabet_symbols(p):
  '''str_alphabet_symbols : SYMBOL COMMA str_alphabet_symbols
                          | SYMBOL'''
  automat.add_alphabet_symbol(p[1])    

def p_str_terminal_nums(p):
  '''str_terminal_nums : NUM COMMA str_terminal_nums
                       | NUM''' 
  automat.add_terminal_state(p[1])                                 

def p_str_edges(p):
  '''str_edges : str_edge COMMA str_edges
               | str_edge'''

def p_str_edge(p):
  '''str_edge : OPARENTHESES NUM SEMICOLON NUM SEMICOLON str_edge_symbols end_edge''' 
  current_edge.init_from_state(p[2])   
  current_edge.init_to_state(p[4])

def p_str_edge_symbols(p):
  '''str_edge_symbols : SYMBOL COMMA str_edge_symbols
                      | SYMBOL'''   
  current_edge.add_symbol(p[1]) 

def p_end_edge(p):
  '''end_edge : CPARENTHESES'''
  automat.add_edge(current_edge)                                                             

def p_error(p):
  raise Exception("Syntax error")

parser = yacc.yacc()

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '.out', 'w')

# обработка входных данных файла
while True:
  try:
    s = input()
  except EOFError:
    break
  if not s:
    continue
  try:
    result = parser.parse(s)
  except Exception as err:
    print("Error: " + str(err))

automat.print_automat()    