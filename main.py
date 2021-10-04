import ply.lex as lex
import sys


class Automata(object):

    def __init__(self, alphabet, terminal_states, states, start_state, edges):
        self.alphabet = alphabet
        self.terminal_states = terminal_states
        self.states = states
        self.start_state = start_state
        self.edges = edges


def print_elem(elem, f):
    for elements in elem:
        f.write(elements)


def printer(a, ans):
    file_out = open(sys.argv[1] + '.out', 'w')
    if ans:
        file_out.write("Input is correct")
    else:
        file_out.write("Input is incorrect")
    file_out.write('\n')
    for x, y in zip(("Alphabet:", "Terminal Vertexes:", "States:", "Start Vertex:"),
                    (a.alphabet, a.terminal_states, a.states, a.start_state)):
        file_out.write(x)
        file_out.write('\n')
        for elem in y:
            print_elem(elem, file_out)
            file_out.write(' ')
        file_out.write('\n')
    file_out.write("Edges:")
    file_out.write('\n')
    for edge in a.edges:
        file_out.write('FROM: ')
        print_elem(edge[0], file_out)
        file_out.write('   ')
        file_out.write('BY: ')
        print_elem(edge[1], file_out)
        file_out.write('   ')
        file_out.write('TO: ')
        for i in range(2, len(edge)):
            print_elem(edge[i], file_out)
            file_out.write(' ')
        file_out.write('\n')
    file_out.close()


correct_input = True

alphabet, terminal_states, states, start_state, edges = list(), list(), list(), list(), list()
with open(sys.argv[1], 'r') as file_in:
    cnt = 0
    while True:
        s = file_in.readline()
        if not s:
            break
        if s == "{\n" or s[0] == '}'    :
            cnt += 1
        else:
            splitted = s.split(' ')
            splitted = [chr(int(e)) for e in splitted]
            if cnt == 1:
                alphabet.append(splitted[0:len(splitted)])
            if cnt == 3:
                terminal_states.append(splitted[0:len(splitted)])
            if cnt == 5:
                states.append(splitted[0:len(splitted)])
            if cnt == 7:
                start_state.append(splitted[0:len(splitted)])
            if cnt == 9:
                letter = file_in.readline()
                letter_splitted = letter.split(' ')
                to = file_in.readline()
                to_splitted = to.split(' ')
                letter_splitted = [chr(int(e)) for e in letter_splitted]
                to_splitted = [chr(int(e)) for e in to_splitted]
                if to != "}\n" and letter != "}\n":
                    edges.append([splitted[0:len(splitted)], letter_splitted[0:len(letter_splitted)], to_splitted[0:len(to_splitted)]])

ans = True

if correct_input:
    a = Automata(alphabet, terminal_states, states, start_state, edges)
    printer(a, ans)
