import sys

keywords: list = ['if', 'else', 'while', ':', ';']
available_types: list = ['int', 'char', 'bool']
error_string: str = 'Error while parsing !'
stop_symbols: list = [' ', ',', ';', '(', ')', '{', '}']
arithmetic_operators: list = ['^', '-', '*', '/', '+', '-']
logic_operators: list = ['==', '/=', '<=', '>=', '<', '>', '!', '&&', '||']
cur_pos: int = 0
s: str = str()
list_of_tokens: list = list()
list_of_functions: list = list()


class Function:

    def __init__(self, name: str, list_of_params: list):
        self.name = name
        self.list_of_params = list_of_params

    def get_arity(self) -> int:
        return len(self.list_of_params)


class Token:

    def __init__(self, token_value: str, token_type: str):
        self.token_value = token_value
        self.token_type = token_type


empty_function = Function('', list())


def skip_spaces_and_porting():
    global cur_pos, s
    while cur_pos < len(s) and (s[cur_pos] == ' ' or s[cur_pos] == '\n'):
        cur_pos += 1


def calc_expr():
    global cur_pos, s
    print(cur_pos)
    try:
        skip_spaces_and_porting()
        if cur_pos >= len(s):
            return

        if s[cur_pos] == '(':
            list_of_tokens.append(Token('(', 'open circular bracket'))
            cur_pos += 1
            return
        if s[cur_pos] == ')':
            list_of_tokens.append(Token(')', 'close circular bracket'))
            cur_pos += 1
            return
        if s[cur_pos] == '{':
            list_of_tokens.append(Token('{', 'open shaped bracket'))
            cur_pos += 1
            return
        if s[cur_pos] == '}':
            list_of_tokens.append(Token('}', 'close shaped bracket'))
            cur_pos += 1
            return

        cur_word: str = str()
        while cur_pos < len(s) and s[cur_pos] not in stop_symbols:
            cur_word += s[cur_pos]
            cur_pos += 1
        skip_spaces_and_porting()

        if cur_word == 'if' or cur_word == 'while':
            if cur_word == 'if':
                list_of_tokens.append(Token('if', 'conditional operator'))
            else:
                list_of_tokens.append(Token('while', 'cycle operator'))

            skip_spaces_and_porting()
            if s[cur_pos] != '(':
                pass

            skip_spaces_and_porting()
            calc_expr()
            skip_spaces_and_porting()

            if s[cur_pos] != ')':
                pass

            skip_spaces_and_porting()
            if s[cur_pos] != '{':
                pass

            skip_spaces_and_porting()
            calc_expr()
            skip_spaces_and_porting()

            if s[cur_pos] != '}':
                pass

        elif cur_word == 'else':
            list_of_tokens.append(Token('else', 'conditional operator'))
            skip_spaces_and_porting()
            if s[cur_pos] != '{':
                pass

            skip_spaces_and_porting()
            calc_expr()
            skip_spaces_and_porting()

            if s[cur_pos] != '}':
                pass

        elif cur_word == ':':
            list_of_tokens.append(Token(':', 'assignment operator'))

        elif cur_word == ';':
            list_of_tokens.append(Token(';', 'linking operator'))

        elif cur_word.isdigit():
            list_of_tokens.append(Token(cur_word, 'number'))

        elif cur_word in list_of_functions:
            list_of_tokens.append(Token(cur_word, 'function'))

        elif cur_word in arithmetic_operators:
            list_of_tokens.append(Token(cur_word, 'arithmetic operator'))

        elif cur_word in logic_operators:
            list_of_tokens.append(Token(cur_word, 'logic operator'))

        elif cur_word[0] == "'":
            list_of_tokens.append(Token(cur_word, 'string'))

        elif cur_word == 'return':
            list_of_tokens.append(Token(cur_word, 'end of function'))

        elif cur_word in available_types:
            list_of_tokens.append(Token(cur_word, 'type'))

        elif cur_word != '':
            list_of_tokens.append(Token(cur_word, 'variable'))

        calc_expr()
    except:
        return


def parse_function(S: str, t: bool) -> Function:
    global s, cur_pos, list_of_functions, list_of_tokens
    if t:
        list_of_functions = list()
        list_of_tokens = list()
    pos = S.find('\n')
    first_line = S[:pos]
    function_interior: str = "{\n" + S[pos + 1:len(S) - 2] + "}\n"
    print(function_interior)
    result_function = parse_function_definition(first_line)
    parse_function_interior(function_interior)
    return result_function


def parse_function_definition(S: str) -> Function:
    global list_of_functions
    tokens: list = S.split(' ')
    name: str = tokens[1]
    list_of_functions.append(name)
    list_of_params: list = list()

    if len(tokens) <= 2 or tokens[2][0] != '(' or tokens[-2][-1] != ')' or tokens[-1][0] != '{':
        print('Error in function definition')
        return empty_function

    tokens[2]: str = tokens[2][1:len(tokens[2])]
    tokens[-2]: str = tokens[-2][0:len(tokens[-2]) - 1]

    for i in range(2, len(tokens) - 1, 2):
        if tokens[i] not in available_types:
            print('Error in function definition')
            return empty_function
        list_of_params.append(tokens[i])

    list_of_tokens.append(Function(name, list_of_params))
    return Function(name, list_of_params)


def parse_function_interior(S: str):
    global s, cur_pos, list_of_functions, list_of_tokens
    cur_pos = 0
    s = S
    while cur_pos < len(s):
        calc_expr()
        cur_pos += 1



def solve(file_name: str, t: bool):
    sys.stdout = open(file_name + '.out', 'w')
    with open(file_name, 'r') as file_in:
        while True:
            s = file_in.readline()
            if not s:
                break
            if s.split(' ')[0] == 'def':
                function_definition = s
                while s[0] != '}':
                    s = file_in.readline()
                    function_definition += s
                print(function_definition)
                f: Function = parse_function(function_definition, t)

        print("Recursive parser output:")
        tmp = 0
        for elem in list_of_tokens:
            if type(elem) == Token:
                if elem.token_value == '{':
                    tmp += 1

                for q in range(tmp):
                    print('\t', end='')
                print("Token( value : '{0}', type = '{1}' )".format(elem.token_value, elem.token_type))
                if elem.token_value == '}':
                    tmp -= 1

            elif type(elem) == Function:
                res: str = "Function( name : {0}, arity : {1}, types of params : [".format(elem.name, elem.get_arity())
                for t in elem.list_of_params:
                    res += t + ', '
                res = res[0:len(res) - 2]
                res += '] )'
                print(res)
