import sys
from parse import parser, ERROR


def check_start(automata):
    if (automata["start"] not in automata["q"]):
        return True
    return False


def check_states(automata):
    if (len(automata["q"]) != len(set(automata["q"]))):
        return True
    return False


def check_sigma(automata):
    if (len(automata["sigma"]) != len(set(automata["sigma"]))):
        return True
    return False


def check_determined(automata):
    d = {x: set() for x in automata["q"]}
    for i in automata["delta"]:
        if (i["symbol"] in d[i["start_state"]]):
            print(d)
            print(i["symbol"])
            return True
        d[i["start_state"]].add(i["symbol"])
    return False

def check_full(automata):
    d = {x: set() for x in automata["q"]}
    for i in automata["delta"]:
        d[i["start_state"]].add(i["symbol"])
        if(i["symbol"] not in automata["sigma"]):
            return True
    for i in d.keys():
        if(len(d[i]) != len(automata["sigma"])):
            return True
def check_automata(automata):
    if (ERROR):
        return "unexpected symbol!"
    if (check_start(automata)):
        return "wrong start state!"
    if (check_states(automata)):
        return "states are not unique!"
    if (check_sigma(automata)):
        return "alphabet symbols are not unique!"
    if(check_determined(automata)):
        return "automata is not determined!"
    if(check_full(automata)):
        return "automata is not full or delta is incorrect!"
    return "Automata is ok!"
fin = open(sys.argv[1], 'r')
result = parser.parse(fin.read())

print(check_automata(result))
