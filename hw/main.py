import ply.lex as lex
import sys


class A(object):

    def __init__(self, alphabet, t_vertexes, states, s_vertex, edges):
        self.alphabet = alphabet
        self.t_vertexes = t_vertexes
        self.states = states
        self.s_vertex = s_vertex
        self.edges = edges


def to_ten_system(S):
    k = 2 ** (len(S) - 1)
    res = int(0)
    for elem in S:
        res += int(elem) * k
        k /= 2
    return res


def print_elem(elem, f):
    for i in range(len(elem) // 8):
        e = elem[8 * i: 8 * (i + 1)]
        f.write(chr(int(to_ten_system(e))))


def printer(a, ans):
    file_out = open(sys.argv[1] + '.out', 'w')
    if ans:
        file_out.write("Этот автомат удовлетвояет всем проверкам")
    else:
        file_out.write("Этот автомат удовлетвояет не всем проверкам")
    file_out.write('\n')
    for x, y in zip(("Alphabet:", "Terminal Vertexes:", "States:", "Start Vertex:"),
                    (a.alphabet, a.t_vertexes, a.states, a.s_vertex)):
        file_out.write(x)
        file_out.write('\n')
        for elem in y:
            print_elem(elem, file_out)
            file_out.write(' ')
        file_out.write('\n')
    file_out.write("Edges:")
    file_out.write('\n')
    for edge in a.edges:
        file_out.write('from: ')
        print_elem(edge[0], file_out)
        file_out.write('   ')
        file_out.write('to: ')
        print_elem(edge[1], file_out)
        file_out.write('   ')
        file_out.write('using: ')
        for i in range(2, len(edge)):
            print_elem(edge[i], file_out)
            file_out.write(' ')
        file_out.write('\n')
    file_out.close()


correct_input = True

alphabet, t_vertexes, states, s_vertex, edges = list(), list(), list(), list(), list()
with open(sys.argv[1], 'r') as file_in:
    while True:
        s = file_in.readline()
        if not s:
            break
        l = s.split(' ')
        l[-1] = l[-1][0:len(l[-1]) - 1]
        if l[0] == 'Alphabet':
            alphabet = l[1:len(l)]
        if l[0] == 'Terminalvertexes':
            t_vertexes = l[1:len(l)]
        if l[0] == 'States':
            states = l[1:len(l)]
        if l[0] == 'Startvertex':
            s_vertex = l[1:len(l)]
        if l[0] == 'Edge':
            edges.append(l[1:len(l)])
        if len(alphabet) == 0 or len(alphabet) == 0 or len(alphabet) == 0 or len(alphabet) == 0:
            file_out = open(sys.argv[1] + '.out', 'w')
            file_out.write("Некорректный ввод !")
            file_out.write('\n')
            file_out.close()
            correct_input = False
        for elem in edges:
            if len(elem) < 3:
                file_out = open(sys.argv[1] + '.out', 'w')
                file_out.write("Некорректный ввод !")
                file_out.write('\n')
                file_out.close()
                correct_input = False

ans = True

# -------------------------------------

if len(s_vertex) != 1:
    ans = False

# -------------------------------------

for i in range(len(states)):
    for j in range(len(states)):
        if i != j and states[i] == states[j]:
            ans = False

# -------------------------------------

for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        if i != j and alphabet[i] == alphabet[j]:
            ans = False

# -------------------------------------

used = dict()
for elem in edges:
    start = elem[0]
    values = elem[2:len(elem)]
    if start not in used:
        used[start] = list()
    for val in values:
        if val in used[start]:
            ans = False
        used[start].append(ans)

# -------------------------------------

used = dict()
for elem in edges:
    start = elem[0]
    values = elem[2:len(elem)]
    if start not in used:
        used[start] = list()
    for val in values:
        used[start].append(ans)
for elem in used:
    if ((elem[0] == '0' or elem[0] == '1') and len(alphabet) != 1) or (len(elem) != len(alphabet) and len(alphabet) > 1):
        ans = False

# -------------------------------------
if correct_input:
    a = A(alphabet, t_vertexes, states, s_vertex, edges)
    printer(a, ans)