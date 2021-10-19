from antlr4 import *
from DKALexer import DKALexer
from DKAVisitor import DKAVisitor
from DKAParser import DKAParser
import sys

from antlr4.tree.Trees import Trees


class EvalVisitor(DKAVisitor):
    def visitStart(self, ctx):
        print("start")
        self.visit(ctx.statesInit())
        self.visit(ctx.alphaInit())
        self.visit(ctx.initialInit())
        self.visit(ctx.terminalInit())
        self.visit(ctx.transInit())

# STATES
    def visitStatesInit(self, ctx):
        print("\t\tSTATES:\n\t\t\t\t", self.visit(ctx.states()))

    def visitStatesContinue(self, ctx):
        return [str(ctx.SYMB().getText())] + self.visit(ctx.states())

    def visitStatesStop(self, ctx):
        return [str(ctx.SYMB().getText())]

# ALPHA
    def visitAlphaInit(self, ctx):
        print("\t\tALPHA:\n\t\t\t\t", self.visit(ctx.states()))

# INITIAL
    def visitInitialInit(self, ctx):
        print("\t\tINITIAL:\n\t\t\t\t", self.visit(ctx.initial()))

    def visitInitial(self, ctx):
        return str(ctx.SYMB().getText())

# ACCEPTING
    def visitTerminalInit(self, ctx):
        print("\t\tACCEPTING:\n\t\t\t\t", self.visit(ctx.states()))

# TRANS
    def visitTransInit(self, ctx):
        print("\t\tTRANS:")
        for edge in self.visit(ctx.edges()):
            print("\t\t\t\t", edge.replace(">", " --> "))

    def visitEdgesContinue(self, ctx):
        return [self.visit(ctx.edge())] + self.visit(ctx.edges())

    def visitEdgesStop(self, ctx):
        return [self.visit(ctx.edge())]

    def visitEdge(self, ctx):
        return str(ctx.getText())


def main():
    if len(sys.argv) != 2:
        print("Need 1 argument: name of input file")
        sys.exit(1)
    file = open(sys.argv[1], "r")
    expression = file.read()
    lexer = DKALexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = DKAParser(stream)
    tree = parser.start()
    # print(Trees.toStringTree(tree, None, parser))
    answer = EvalVisitor().visit(tree)
    print(answer)


if __name__ == '__main__':
    main()
