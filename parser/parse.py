import ply.lex as lex
import sys

tokens = [
  'EDGE',
  'VERTEX',
  'TERMINAL',
  'ARROW',
  'COLON',
  'QUOTES',
  'SEMICOLON',
  'NUM'
]

class Automate:
  cnt = 0
  alphabet = []
  edges = []
  dic = {}
  vertexes = []
  def print():
    fout = open(sys.argv[1] + '.out', 'w')
    fout.write("alphabet:\n")
    for i in Automate.alphabet:
      fout.write(i+'\n')
    if ('Q0' in Automate.dic):
      fout.write("Q0 is initial state\n")
    else:
      fout.write("T0 is initial state\n")
    for i in Automate.dic:
      for j in Automate.dic[i]:
        fout.write("Edge from " + i + " to " + Automate.dic[i][j] + " by \"" + Automate.alphabet[int(j)-1] + "\"\n")
    fout.close

def t_EDGE(t):
  r'"(.)+"(?=\n)'
  t.value = t.value[1:-1]
  return t

def t_VERTEX(t):
  r'Q([1-9][0-9]*|0)'
  return t

def t_TERMINAL(t):
  r'T([1-9][0-9]*|0)'
  return t

t_ARROW = r'->'
t_COLON = r':'
t_QUOTES = r'"'
t_SEMICOLON = r';'
t_NUM = r'([1-9][0-9]*|0)'
t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  exit()

def write_error(t):
  fout = open(sys.argv[1] + '.out', 'w')
  if (not t):
    fout.write("Illegal format")
  else:
    fout.write("Illegal format: line " + str(t.lineno) + " pos " + str(t.lexpos))
  fout.close()

def write_ans():
  if (('Q0' not in Automate.dic) and ('T0' not in Automate.dic)):
    print_err("Error: there is no started vertex in automaton")
  for i in set(Automate.vertexes):
    if (i not in Automate.dic):
      print_err("Error: there is no started vertex in automaton")
  for i in Automate.dic:
    if (len(Automate.dic[i]) != Automate.cnt):
      print_err("Error: automaton is not complete, vertex " + i + " have not enough edges\n")
    if (i[0] == 'Q'):
      s = 'T' + i[1:] 
    else:
      s = 'Q' + i[1:]
    if (s in Automate.dic):
      print_err("Error: vertex " + s[1:] + " have terminal and nonterminal versions")
  Automate.print()

def print_err(str):
  fout = open(sys.argv[1] + '.out', 'w')
  fout.write(str)
  fout.close()
  exit()

def main():
  lexer = lex.lex()
  fin = open(sys.argv[1], 'r')
  lexer.input(fin.read())
  fin.close()
  tok = lexer.token()
  if ((not tok) or (tok.type != 'NUM')):
    write_error(tok)
    return
  else:
    Automate.cnt = int(tok.value)
    for i in range(int(Automate.cnt)):
      tok = lexer.token()
      if ((not tok) or (tok.type != 'EDGE')):
        write_error(tok)
        return
      else:
        if (tok.value in Automate.alphabet):
          print_err("Error: the string " + tok.value + " is found twice in the alphabet")
        Automate.alphabet.append(tok.value)
  if (Automate.cnt != len(Automate.alphabet)):
    print_err("Error: wrong size of alphabet")
  tok = lexer.token()
  while True:
    if (not tok):
      break
    elif ((tok.type != 'VERTEX') and (tok.type != 'TERMINAL')):
      write_error(tok)
      return
    else:
      Automate.vertexes.append(tok.value)
      t = lexer.token()
      if ((not t) or (t.type != 'COLON')):
        write_error(t)
        return
      else:
        while True:
          tok2 = lexer.token()
          if (not tok2):
            tok = tok2
            break
          elif (tok2.type == 'NUM'):
            t = lexer.token()
            if ((not t) or (t.type != 'ARROW')):
              write_error(t)
              return
            tok3 = lexer.token()
            if ((not tok3) or ((tok3.type != 'TERMINAL') and (tok3.type != 'VERTEX'))):
              write_error(tok3)
              return
            t = lexer.token()
            if ((not t) or (t.type != 'SEMICOLON')):
              write_error(t)
              return
            Automate.vertexes.append(tok3.value)
            if (tok.value in Automate.dic):
              if (tok2.value in Automate.dic[tok.value]):
                print_err("Error: automaton is not deterministic because from " + tok.value + " two edges by \"" + tok2.value + "\"\n")
              else:
                Automate.dic[tok.value].update({tok2.value : tok3.value})  
            else:
              Automate.dic[tok.value] = {tok2.value : tok3.value}
            Automate.edges.append((tok.value, tok2.value, tok3.value))
          else:
            tok = tok2
            break
  write_ans()
main()
