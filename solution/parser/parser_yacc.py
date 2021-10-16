import ply.lex as lex
import ply.yacc as yacc
import sys

file_out = open(sys.argv[1] + ".out", 'w')
stack = ["v_0"]
index_of_object = 0
index_of_vertex = 1
last_if = ""
tokens = (
    'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN', 'NUMBER', 'SEMICOLON', 'NEWLINE', 'VARIABLE', 'STRING', 'NOT',
    'IF', 'FOR', 'ELSE', 'FOR_BEGIN', 'FOR_END', 'FOR_NEXT', 'BEGIN', 'END', 'TYPE', 'EQUAL', 'DEGREE', 'EQUAL2',
    'NOTEQUAL', 'LESSEQUAL', 'MOREEQUAL', 'LESS', 'MORE', 'AND', 'OR', 'COMA', 'RETURN', 'METHODTYPE', 'OPERATOR', 'OP')

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
t_FOR_BEGIN = r'\['
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
    r"""int|binint|string"""
    return t


def t_METHODTYPE(t):
    r"""p\_int|p\_binint|p\_string"""
    return t


def t_RETURN(t):
    r"""return"""
    return t


def t_NUMBER(t):
    r"""[0-9]+"""
    return t


def t_OPERATOR(t):
    r"""o\_[^\s|^\(]+"""
    return t


def t_OP(t):
    r"""operator\_[0-9]+\_[0-9]+"""
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
    is_skip = False
    for i in range(0, len(s)):
        if is_skip:
            is_skip = False
            continue
        if s[i] == '>':
            result += "&gt;"
        elif s[i] == '<':
            result += "&lt;"
        elif s[i] == '&':
            result += "&amp;"
        elif s[i] == ' ':
            continue
        elif i < len(s) - 1 and (s[i] + s[i + 1]) == "o_":
            is_skip = True
            continue
        else:
            result += s[i]
    return result


def create_name(name):
    global index_of_vertex
    result = "v_" + str(index_of_vertex)
    index_of_vertex += 1
    file_out.write(result + " [label=<" + name + ">]\n")
    return result


def create_body_vertex():
    global index_of_object
    new_body_name = create_name("Body")
    for i in range(1, index_of_object + 1):
        add_edge(new_body_name, stack[-i])
    for i in range(0, index_of_object):
        stack.pop()
    index_of_object = 0
    return new_body_name


def p_if(p):
    """expr : IF LPAREN expr RPAREN BEGIN expr END
            | IF LPAREN expr RPAREN BEGIN NEWLINE expr END
            | IF LPAREN expr RPAREN BEGIN expr NEWLINE END
            | IF LPAREN expr RPAREN BEGIN NEWLINE expr NEWLINE END"""
    global last_if, index_of_object
    print(index_of_vertex, "if")
    new_if_vertex = create_name("If statement")
    new_cond_vertex = create_name("Condition")
    add_edge(new_if_vertex, create_body_vertex())
    add_edge(new_if_vertex, new_cond_vertex)
    add_edge(new_cond_vertex, stack[-1])
    stack.pop()
    stack.append(new_if_vertex)
    last_if = new_if_vertex


def p_else(p):
    """expr : ELSE BEGIN expr END
            | ELSE BEGIN NEWLINE expr END
            | ELSE BEGIN expr NEWLINE END
            | ELSE BEGIN NEWLINE expr NEWLINE END"""
    global last_if, index_of_object
    print(index_of_vertex, "else")
    new_vertex = create_name("Else statement")
    add_edge(new_vertex, create_body_vertex())
    add_edge(last_if, new_vertex)
    index_of_object -= 1


def p_for(p):
    """expr : FOR expr FOR_END BEGIN expr END
            | FOR expr FOR_END BEGIN NEWLINE expr END
            | FOR expr FOR_END BEGIN expr NEWLINE END
            | FOR expr FOR_END BEGIN NEWLINE expr NEWLINE END"""
    print(index_of_vertex, "for")
    global index_of_object
    new_for_vertex = create_name("For statement")
    new_cond_vertex = create_name("Condition")
    add_edge(new_for_vertex, new_cond_vertex)
    add_edge(new_for_vertex, create_body_vertex())
    add_edge(new_for_vertex, stack[-1])
    stack.pop()
    add_edge(new_for_vertex, stack[-1])
    stack.pop()
    add_edge(new_cond_vertex, stack[-1])
    stack.pop()
    stack.append(new_for_vertex)


def p_expr_end(p):
    """expr : expr SEMICOLON NEWLINE expr
            | expr SEMICOLON expr
            | expr SEMICOLON NEWLINE
            | expr SEMICOLON"""
    global index_of_object
    print(index_of_vertex, "expr end")
    index_of_object += 1


def p_for_next(p):
    """expr : expr FOR_BEGIN expr
            | expr FOR_BEGIN
            | FOR_BEGIN expr"""
    global index_of_object
    print(index_of_vertex, "for begin")
    index_of_object = 0


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
            | expr OR expr
            | expr OPERATOR expr"""
    print(index_of_vertex, "operator")
    new_vertex = create_name("Operator=\"" + operator_checking(str(p[2])) + "\"")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_var_assigment(p):
    """expr : expr EQUAL expr"""
    global index_of_object
    print(index_of_vertex, "var assigment")
    new_vertex = create_name("Variable assignment")
    add_edge(new_vertex, stack[-index_of_object])
    del stack[-index_of_object]
    add_edge(new_vertex, stack[-index_of_object])
    del stack[-index_of_object]
    stack.append(new_vertex)


def p_var_init(p):
    """expr : TYPE expr EQUAL expr"""
    global index_of_object
    print(index_of_vertex, "var init")
    new_vertex = create_name("Variable init")
    add_edge(new_vertex, create_name("Type=\"" + p[1] + "\""))
    add_edge(new_vertex, stack[-index_of_object])
    del stack[-index_of_object]
    add_edge(new_vertex, stack[-index_of_object])
    del stack[-index_of_object]
    stack.append(new_vertex)


def p_return(p):
    """expr : RETURN expr"""
    global index_of_object
    print(index_of_vertex, "return")
    new_vertex = create_name("Return")
    add_edge(new_vertex, stack[-index_of_object])
    del stack[-index_of_object]
    stack.append(new_vertex)


def p_method_init(p):
    """expr : TYPE VARIABLE LPAREN expr RPAREN BEGIN expr END
            | TYPE VARIABLE LPAREN expr RPAREN BEGIN NEWLINE expr END
            | TYPE VARIABLE LPAREN expr RPAREN BEGIN expr NEWLINE END
            | TYPE VARIABLE LPAREN expr RPAREN BEGIN NEWLINE expr NEWLINE END
            | TYPE VARIABLE LPAREN RPAREN BEGIN expr END
            | TYPE VARIABLE LPAREN RPAREN BEGIN NEWLINE expr END
            | TYPE VARIABLE LPAREN RPAREN BEGIN expr NEWLINE END
            | TYPE VARIABLE LPAREN RPAREN BEGIN NEWLINE expr NEWLINE END"""
    global index_of_object
    print(index_of_vertex, "method init")
    new_vertex = create_name("Method")
    add_edge(new_vertex, create_name("Type=\"" + p[1] + "\""))
    add_edge(new_vertex, create_name("Name=\"" + p[2] + "\""))
    add_edge(new_vertex, create_body_vertex())
    if p[4] != ')':
        add_edge(new_vertex, stack[-1])
        del stack[-1]
    stack.append(new_vertex)


def p_operator_init(p):
    """expr : TYPE OP OPERATOR LPAREN expr RPAREN BEGIN expr END
            | TYPE OP OPERATOR LPAREN expr RPAREN BEGIN NEWLINE expr END
            | TYPE OP OPERATOR LPAREN expr RPAREN BEGIN expr NEWLINE END
            | TYPE OP OPERATOR LPAREN expr RPAREN BEGIN NEWLINE expr NEWLINE END
            | TYPE OP OPERATOR LPAREN RPAREN BEGIN expr END
            | TYPE OP OPERATOR LPAREN RPAREN BEGIN NEWLINE expr END
            | TYPE OP OPERATOR LPAREN RPAREN BEGIN expr NEWLINE END
            | TYPE OP OPERATOR LPAREN RPAREN BEGIN NEWLINE expr NEWLINE END"""
    global index_of_object
    print(index_of_vertex, "method init")
    new_vertex = create_name("Operator")
    add_edge(new_vertex, create_name("Type=\"" + p[1] + "\""))
    add_edge(new_vertex, create_name("Name=\"" + operator_checking(p[3]) + "\""))
    add_edge(new_vertex, create_name("Priority=\"" + p[2].split('_')[1] + "\""))
    add_edge(new_vertex, create_name("Associativity=\"" + p[2].split('_')[2] + "\""))
    add_edge(new_vertex, create_body_vertex())
    if p[5] != ')':
        add_edge(new_vertex, stack[-1])
        del stack[-1]
    stack.append(new_vertex)


def p_operator_par(p):
    """expr : expr COMA expr"""
    print(index_of_vertex, "parameter")
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
    new_vertex = create_name("Method assignment")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    add_edge(new_vertex, create_name("Name=\"" + p[1] + "\""))
    stack.append(new_vertex)


def p_parens(p):
    """expr : LPAREN expr RPAREN"""
    print(index_of_vertex, "brackets")
    new_vertex = create_name("Brackets")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_not(p):
    """expr : NOT expr %prec UNOT"""
    print(index_of_vertex, "not")
    new_vertex = create_name("Not")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_uminus(p):
    """expr : MINUS expr %prec UMINUS"""
    print(index_of_vertex, "unary minus")
    new_vertex = create_name("Unary minus")
    add_edge(new_vertex, stack[-1])
    stack.pop()
    stack.append(new_vertex)


def p_num(p):
    """expr : NUMBER"""
    print(index_of_vertex, "number")
    new_vertex = create_name("Number=\"" + str(p[1]) + "\"")
    stack.append(new_vertex)


def p_init_empty(p):
    """expr : METHODTYPE VARIABLE"""
    print(index_of_vertex, "type var")
    new_vertex = create_name("Variable=\"" + p[2] + "\"")
    add_edge(new_vertex, create_name("Type=\"" + p[1][2::] + "\""))
    stack.append(new_vertex)


def p_var(p):
    """expr : VARIABLE"""
    print(index_of_vertex, "variable")
    new_vertex = create_name("Variable=\"" + p[1] + "\"")
    stack.append(new_vertex)


def p_string(p):
    """expr : STRING"""
    print(index_of_vertex, "string")
    new_vertex = create_name("String=" + p[1])
    stack.append(new_vertex)


def p_error(p):
    print("Syntax error in input!", p)


def main():
    file_out.write("digraph {\n")
    file_out.write("v_0 [label=<root>]\n")
    parser = yacc.yacc()
    file_in = open(sys.argv[1], 'r')
    parser.parse(file_in.read())
    for i in range(1, len(stack)):
        add_edge(stack[0], stack[-i])
    file_out.write("}\n")
    file_out.close()


main()
