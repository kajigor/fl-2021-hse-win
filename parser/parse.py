import ply.yacc as yacc
from lex import tokens
import sys

# автомат -- граф, характеризуется состояними (вершины Vertex) и ребрами перехода (ребра Edges)

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

class Automaton:
  def __init__(self):
    self.alphabet_size = 0
    self.alphabet = []
    self.count_states = 0
    self.start_state = 0
    self.count_terminal = 0
    self.terminal_states = []
    self.count_edges = 0
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

  def init_count_edges(self, count):
    self.count_edges = count

  def add_edge(self, edge):
    self.edges.append(edge)  

  def print_automaton(self):
    print("Alphabet:\n    ", end="")
    print(self.alphabet)

    print("Start: ", end="")
    print(self.start_state)

    print("Terminals:\n    ", end="")
    print(self.terminal_states)

    print("Edges:\n")
    for edge in self.edges:
      print("    " + edge.from_state + " --> " + edge.to_state + " (")
      print(edge.symbols)
      print(" )\n")

def p_automaton(p):
  '''Automaton : Alphabet
               | States_count
               | Start_state
               | Terminals
               | Edges '''

def p_alphabet(p):
  'Alphabet : ALPHABET COLON NUM DASH OPARENTHESES str_alphabet_symbols CPARENTHESES'
  parser.current_obj_for_reading = "alphabet"

def p_states_count(p):
  'States_count : Q COLON NUM'
  parser.current_obj_for_reading = "states count"
  parser.automaton.init_count_states(10)

def p_start_state(p):
  'Start_state : START COLON NUM'
  parser.current_obj_for_reading = "start state"
  parser.automaton.init_start_state(p[3])

def p_terminals(p):
  'Terminals : T COLON NUM DASH str_nums'

def p_edges(p):
  'Edges : EDGES COLON str_edges'

def p_str_alphabet_symbols(p):
  '''str_alphabet_symbols : SYMBOL COMMA str_alphabet_symbols
                          | SYMBOL'''

def p_str_edges(p):
  '''str_edges : str_edge COMMA str_edges
               | str_edge'''

def p_str_edge(p):
  '''str_edge : OPARENTHESES NUM SEMICOLON NUM SEMICOLON str_nums CPARENTHESES'''   

def p_str_nums(p):
  '''str_nums : NUM COMMA str_nums
              | NUM'''                                               

def p_error(p):
  raise Exception("Syntax error")

parser = yacc.yacc()

parser.automaton = Automaton()
parser.current_obj_for_reading = ""
parser.current_edge = Edge()

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

parser.automaton.print_automaton()    






