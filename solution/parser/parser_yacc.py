import ply.lex as lex
import ply.yacc as yacc

file_out = open("output.dot", 'w')
stack = ["v_0"]
stack_object_size = []
index_of_vertex = 1
is_else = False
tokens = (
    'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN', 'NUMBER', 'SEMICOLON', 'NEWLINE', 'VARIABLE', 'STRING', 'NOT',
    'IF', 'FOR', 'ELSE', 'FOR_START', 'FOR_END', 'FOR_NEXT', 'BEGIN', 'END', 'TYPE', 'EQUAL', 'DEGREE', 'EQUAL2',
    'NOTEQUAL', 'LESSEQUAL', 'MOREEQUAL', 'LESS', 'MORE', 'AND', 'OR', 'COMA')

t_ignore = ' \t'
t_NEWLINE = r'\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_VARIABLE = r'\w+'
t_STRING = r'\"[^\"]*\"'
t_NOT = r'!'
t_ELSE = r'else'
t_FOR_START = r'\['
t_FOR_END = r'\]'
t_FOR_NEXT = r'\|'
t_BEGIN = r'\{'
t_END = r'\}'
t_EQUAL = r'='
t_DEGREE = r'\^'
t_EQUAL2 = r'=='
t_NOTEQUAL = r'\/='
t_LESSEQUAL = r'<='
t_LESS = r'<'
t_MOREEQUAL = r'>='
t_MORE = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_COMA = r'\,'


def t_IF(t):
    r"""if"""
    return t


def t_FOR(t):
    r"""for"""
    return t


def t_TYPE(t):
    r"""int"""
    return t


def t_NUMBER(t):
    r"""[0-9]+"""
    t.value = int(t.value)
    return t


def t_error(t):
    print("Invalid Token:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS', 'MULT', 'DIV'),
    ('right', 'DEGREE', 'AND', 'OR'),
    ('nonassoc', 'UMINUS', 'UNOT', 'EQUAL2', 'NOTEQUAL', 'LESSEQUAL', 'MOREEQUAL', 'LESS', 'MORE')
)


def add_edge(a, b):
    file_out.write(a + " -> " + b + "\n")


def operator_checking(s):
    result = ""
    for ch in s:
        if ch == '>':
            result += "&gt;"
        elif ch == '<':
            result += "&lt;"
        elif ch == '&':
            result += "&amp;"
        elif ch != ' ':
            result += ch
    return result


def create_name(name):
    global index_of_vertex
    result = "v_" + str(index_of_vertex)
    index_of_vertex += 1
    file_out.write(result + " [label=<" + name + ">]\n")
    return result


def p_operator(p):
    """expr : expr PLUS expr
            | expr MINUS expr
            | expr MULT expr
            | expr DIV expr
            | expr DEGREE expr
            | expr EQUAL2 expr
            | expr NOTEQUAL expr
            | expr LESSEQUAL expr
            | expr MOREEQUAL expr
            | expr LESS expr
            | expr MORE expr
            | expr AND expr
            | expr OR expr"""
    # TODO think how to add new operator
    print(index_of_vertex, "operator")
    print(stack)
    new_vertex = create_name("Operator=\"" + operator_checking(str(p[2])) + "\"")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_uminus(p):
    """expr : MINUS expr %prec UMINUS"""
    print(index_of_vertex, "unary minus")
    print(stack)
    new_vertex = create_name("Unary minus")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_num(p):
    """expr : NUMBER"""
    print(index_of_vertex, "number")
    print(stack)
    new_vertex = create_name("Number=\"" + str(p[1]) + "\"")
    stack.append(new_vertex)


def p_var(p):
    """expr : VARIABLE"""
    print(index_of_vertex, "variable")
    print(stack)
    new_vertex = create_name("Variable=\"" + p[1] + "\"")
    stack.append(new_vertex)


def p_string(p):
    """expr : STRING"""
    print(index_of_vertex, "string")
    print(stack)
    new_vertex = create_name("String=" + p[1])
    stack.append(new_vertex)


def p_not(p):
    """expr : NOT expr %prec UNOT"""
    print(index_of_vertex, "not")
    print(stack)
    new_vertex = create_name("Not")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_parens(p):
    """expr : LPAREN expr RPAREN"""
    print(index_of_vertex, "brackets")
    print(stack)
    new_vertex = create_name("Brackets")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_var_init(p):
    """expr : TYPE expr EQUAL expr"""
    print(index_of_vertex, "var init")
    print(stack)
    new_vertex = create_name("Variable init")
    add_edge(new_vertex, create_name("Type=\"" + p[1] + "\""))
    add_edge(new_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_var_assigment(p):
    """expr : expr EQUAL expr"""
    print(index_of_vertex, "var assigment")
    print(stack)
    new_vertex = create_name("Variable assignment")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_operator_par(p):
    """expr : expr COMA expr"""
    print(index_of_vertex, "parameter")
    print(stack)
    new_vertex = create_name("Parameter")
    new_next_vertex = create_name("Next")
    add_edge(new_vertex, new_next_vertex)
    add_edge(new_next_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_method_assignment(p):
    """expr : VARIABLE LPAREN expr RPAREN"""
    print(index_of_vertex, "method assigment")
    print(stack)
    new_vertex = create_name("Method assignment")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, create_name("Name=\"" + p[1] + "\""))
    stack.append(new_vertex)


def p_if(p):
    """expr : IF LPAREN expr RPAREN BEGIN expr END
            | IF LPAREN expr RPAREN BEGIN NEWLINE expr END
            | IF LPAREN expr RPAREN BEGIN expr NEWLINE END
            | IF LPAREN expr RPAREN BEGIN NEWLINE expr NEWLINE END"""
    global is_else, stack_object_size
    print(index_of_vertex, "if")
    print(stack)
    new_if_vertex = create_name("If statement")
    new_cond_vertex = create_name("Condition")
    new_body_name = create_name("Body")
    for i in range(1, stack_object_size[-1] + 1):
        add_edge(new_body_name, stack[-i])
    for i in range(0, stack_object_size[-1]):
        stack.pop()
    stack_object_size.pop()
    add_edge(new_if_vertex, new_body_name)
    add_edge(new_if_vertex, new_cond_vertex)
    if is_else:
        add_edge(new_if_vertex, stack[-1])
        stack.pop()
    add_edge(new_cond_vertex, stack[-1])
    stack.pop()
    stack.append(new_if_vertex)
    is_else = False


# def p_body(p):
#     """expr : BEGIN expr END
#             | BEGIN NEWLINE expr END
#             | BEGIN expr NEWLINE END
#             | BEGIN NEWLINE expr NEWLINE END"""
#     global stack_object_size
#     print(index_of_vertex, "body")
#     print(stack)
#     new_vertex = create_name("Body")
#     for i in range(1, stack_object_size[-1] + 1):
#         add_edge(new_vertex, stack[-i])
#     for i in range(0, stack_object_size[-1]):
#         stack.pop()
#     stack_object_size.pop()
#     stack.append(new_vertex)


def p_else(p):
    """expr : ELSE BEGIN expr END
            | ELSE BEGIN NEWLINE expr END
            | ELSE BEGIN expr NEWLINE END
            | ELSE BEGIN NEWLINE expr NEWLINE END"""
    global is_else
    print(index_of_vertex, "else")
    print(stack)
    is_else = True
    new_vertex = create_name("Else statement")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_for(p):
    """expr : FOR FOR_START expr FOR_NEXT expr FOR_NEXT expr FOR_END expr"""
    print(index_of_vertex, "for")
    print(stack)
    new_for_vertex = create_name("For statement")
    new_cond_vertex = create_name("Condition")
    add_edge(new_for_vertex, new_cond_vertex)
    add_edge(new_for_vertex, stack[-1])
    stack.pop()
    add_edge(new_for_vertex, stack[-1])
    stack.pop()
    add_edge(new_cond_vertex, stack[-1])
    stack.pop()
    add_edge(new_for_vertex, stack[-1])
    stack.pop()
    stack.append(new_for_vertex)


def p_expr_end(p):
    """expr : expr SEMICOLON NEWLINE expr
            | expr SEMICOLON expr
            | expr SEMICOLON NEWLINE
            | expr SEMICOLON"""
    print(index_of_vertex, "expr end")
    print(stack)


def p_error(p):
    print("Syntax error in input!", p)


def fill_stack_object_size(code):
    global stack_object_size
    tmp = [0]
    for ch in code:
        if ch == ';':
            tmp[-1] += 1
        if ch == '{':
            tmp.append(0)
        if ch == '}':
            stack_object_size.append(tmp[-1])
            tmp.pop()
    stack_object_size.append(tmp[-1])
    stack_object_size.reverse()
    print(stack_object_size)


def main():
    file_out.write("digraph {\n")
    file_out.write("v_0 [label=<root>]\n")
    parser = yacc.yacc()
    file_in = open("input.txt", 'r')
    code = file_in.read()
    fill_stack_object_size(code)
    parser.parse(code)
    for i in range(1, len(stack)):
        add_edge(stack[0], stack[-i])
    file_out.write("}\n")
    file_out.close()


main()
