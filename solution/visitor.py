from antlr4 import *
from DKALexer import DKALexer
from DKAVisitor import DKAVisitor
from DKAParser import DKAParser
import sys

from antlr4.tree.Trees import Trees


class EvalVisitor(DKAVisitor):
    def visitStart(self, ctx):
        print(ctx.getText())
        self.visit(ctx.statesInit())
        self.visit(ctx.alphaInit())
        self.visit(ctx.initialInit())
        self.visit(ctx.terminalInit())
        self.visit(ctx.transInit())

# STATES
    def visitStatesInit(self, ctx):
        print("STATES =", self.visit(ctx.states()))

    def visitStatesContinue(self, ctx):
        return [ctx.STATE().getText()] + self.visit(ctx.states())

    def visitStatesStop(self, ctx):
        return [ctx.STATE().getText()]

# ALPHA
    def visitAlphaInit(self, ctx):
        # print(ctx.alphabet().getText())
        for i in list(ctx.alphabet().getChildren())[0::2]:
            print(i.getText(), end="  ")
        # print("ALPHA =", self.visit(ctx.alphabet()))

    def visitAlpabet(self, ctx):
        print("alphabet")
        return

    def visitAlphaContinue(self, ctx):
        print("alpha continue")
        return [ctx.ALPHA().getText()] + self.visit(ctx.alphabet())

    def visitAlphaStop(self, ctx):
        print("alpha stop")
        return [ctx.ALPHA().getText()]

# INITIAL
    def visitInitialInit(self, ctx):
        print("INITIAL =", self.visit(ctx.initial()))

    def visitInitial(self, ctx):
        return ctx.STATE().getText()

# TERMINAL
    def visitTerminalInit(self, ctx):
        print(f"TERMINAL =", self.visit(ctx.states()))

# TRANS
    def visitTransInit(self, ctx):
        print(ctx.edges().getText())
        print("TRANS =", self.visit(ctx.edges()))

    def visitEdgesContinue(self, ctx):
        print("edges continue")
        return [self.visit(ctx.edge())] + self.visit(ctx.edges())

    def visitEdgesStop(self, ctx):
        print("edges stop")
        return [self.visit(ctx.edge())]

    def visitEdge(self, ctx):
        print("edge")
        return [ctx.STATE().getText(), ctx.ALPHA().getText(), ctx.STATE().getText()]

    # def visitOpExpr(self, ctx):
    #
    #     left = self.visit(ctx.left)
    #     right = self.visit(ctx.right)
    #     op = ctx.op.text
    #
    #     opchar1 = op[0]
    #     if opchar1 == '*':
    #         val = left * right
    #     elif opchar1 == '/':
    #         val = left / right
    #     elif opchar1 == '+':
    #         val = left + right
    #     elif opchar1 == '-':
    #         val = left - right
    #     else:
    #         raise ValueError("Unknown operator " + op)
    #     print("visitOpExpr", opchar1, left, right, val)
    #     return val

    # def visitStart(self, ctx):
    #     print("visitStart", ctx.getText())
    #     return self.visit(ctx.expr())

    # def visitAtomExpr(self, ctx):
    #     print("visitAtomExpr", int(ctx.getText()))
    #     return int(ctx.getText())

    # def visitParenExpr(self, ctx):
    #     print("visitParenExpr", ctx.getText())
    #     return self.visit(ctx.expr())


def main():
    if len(sys.argv) != 2:
        print("Need 1 argument: name of input file")
        sys.exit(1)
    file = open(sys.argv[1], "r")
    expression = file.read()
    expression =\
        "states=[q1,q2,q3,q4]\nalpha=[a,b,c,d]\ninitial=[q1]\nterminal=[q4]\ntrans=[q1>a>q2,q1>c>q1,q2>b>q4,q1>b>q3,q3>a>q4,q4>b>q2,q4>c>q4,q2>a>q3,q2>a>q1]"
    lexer = DKALexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = DKAParser(stream)
    tree = parser.start()
    print(Trees.toStringTree(tree, None, parser))
    answer = EvalVisitor().visit(tree)
    print(answer)


if __name__ == '__main__':
    main()
