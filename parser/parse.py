import enum

import ply.yacc as yacc

from lex import tokens


class ConstructorType(enum.Enum):
    enumeration = 0
    strict = 1
    describe = 2


class Alphabet:
    def __init__(self, name, arg_type, constructor_type, constructor_params):
        self.name = name
        self.arg_type = arg_type
        self.constructor_type = constructor_type
        self.constructor_params = constructor_params

    def add_param(self, param):
        self.constructor_params.append(param)

    def __str__(self):
        params_str = ""
        for par in self.constructor_params:
            params_str += "\t\t"
            params_str += par.__str__()

        return str("Alphabet:\n\tname: " +
                   self.name + "\n\targ_type: " +
                   self.arg_type.__str__() + "\n\tconstructor_type: " +
                   self.constructor_type.__str__() + "\n\tconstructor_params:\n" +
                   params_str)


class Variable:
    def __init__(self, vartype, constructor_params):
        self.vartype = vartype
        self.constructor_params = constructor_params

    def add_param(self, param):
        self.constructor_params.append(param)

    def __str__(self):
        params_str = ""
        for par in self.constructor_params:
            params_str += "\t\t"
            params_str += par.__str__()

        return str("Variable:\n\tvartype:" +
                   self.vartype + "\n\tconstructor_params:\n" +
                   params_str)


def p_alphabet(p):
    '''alphabet : DEF ID TYPIZATION CLASSNAME EQUALITY BLOCKSTART enumeration BLOCKEND
                | DEF ID TYPIZATION CLASSNAME EQUALITY CLASSNAME METHOD PARSTART enumeration PAREND
                | DEF ID TYPIZATION CLASSNAME EQUALITY CLASSNAME METHOD BLOCKSTART alphabetdescribebody BLOCKEND
                 '''
    if len(p) == 8:
        p[0] = Alphabet(p[2], (p[3][8:])[:-1], ConstructorType.enumeration, p[7])
    else:
        if len(p) == 10:
            if p[8].type == "PARSTART":
                p[0] = Alphabet(p[2], (p[3][8:])[:-1], ConstructorType.strict, p[9])
            else:
                if p[8].type == "BLOCKSTART":
                    p[0] = Alphabet(p[2], (p[3][8:])[:-1], ConstructorType.describe, p[9])
                else:
                    print("Error: Incorrect alphabet definition at " + p[8].lineno + ":" + p[8].lexpos)
        else:
            print("Error: Incorrect alphabet definition at " + p[1].lineno + ":" + p[1].lexpos)


def p_enumeration(p):
    '''enumeration : term
                    | enumeration COMMA term
                '''
    if len(p) == 1:
        p[0] = [p[1]]
    else:
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            print("Error: Incorrect enumeration at " + p[1].lineno + ":" + p[1].lexpos)


def p_term(p):
    '''term : CHAR
            | INT
            | STRING
            | ID
            | CLASSNAME PARSTART enumeration PAREND
            '''
    if len(p) == 1:
        p[0] = p[1]
    else:
        if len(p) == 4:
            p[0] = Variable(p[1], p[3])
        else:
            print("Error: Incorrect term at " + p[1].lineno + ":" + p[1].lexpos)


def p_alphabetdescribebody(p):
    '''alphabetdescribebody : paramsdescribe
                            | alphabetdescribebody COMMA paramsdescribe
                            '''
    if len(p) == 1:
        p[0] = [p[1]]
    else:
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            print("Error: Incorrect describe body at " + p[1].lineno + ":" + p[1].lexpos)


def p_paramsdescribe(p):
    'paramsdescribe : enumeration FROM ID'
    p[0] = p[1], p[3]


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
    result = parser.parse(s)
    print(result)
