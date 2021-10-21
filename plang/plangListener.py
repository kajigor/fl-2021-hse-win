# Generated from plang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .plangParser import plangParser
else:
    from plangParser import plangParser

# This class defines a complete listener for a parse tree produced by plangParser.
class plangListener(ParseTreeListener):

    # Enter a parse tree produced by plangParser#start.
    def enterStart(self, ctx:plangParser.StartContext):
        pass

    # Exit a parse tree produced by plangParser#start.
    def exitStart(self, ctx:plangParser.StartContext):
        pass


    # Enter a parse tree produced by plangParser#program.
    def enterProgram(self, ctx:plangParser.ProgramContext):
        pass

    # Exit a parse tree produced by plangParser#program.
    def exitProgram(self, ctx:plangParser.ProgramContext):
        pass


    # Enter a parse tree produced by plangParser#relationship.
    def enterRelationship(self, ctx:plangParser.RelationshipContext):
        pass

    # Exit a parse tree produced by plangParser#relationship.
    def exitRelationship(self, ctx:plangParser.RelationshipContext):
        pass


    # Enter a parse tree produced by plangParser#string.
    def enterString(self, ctx:plangParser.StringContext):
        pass

    # Exit a parse tree produced by plangParser#string.
    def exitString(self, ctx:plangParser.StringContext):
        pass


    # Enter a parse tree produced by plangParser#argument.
    def enterArgument(self, ctx:plangParser.ArgumentContext):
        pass

    # Exit a parse tree produced by plangParser#argument.
    def exitArgument(self, ctx:plangParser.ArgumentContext):
        pass


    # Enter a parse tree produced by plangParser#atom.
    def enterAtom(self, ctx:plangParser.AtomContext):
        pass

    # Exit a parse tree produced by plangParser#atom.
    def exitAtom(self, ctx:plangParser.AtomContext):
        pass


    # Enter a parse tree produced by plangParser#goal.
    def enterGoal(self, ctx:plangParser.GoalContext):
        pass

    # Exit a parse tree produced by plangParser#goal.
    def exitGoal(self, ctx:plangParser.GoalContext):
        pass


    # Enter a parse tree produced by plangParser#arithmetic.
    def enterArithmetic(self, ctx:plangParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by plangParser#arithmetic.
    def exitArithmetic(self, ctx:plangParser.ArithmeticContext):
        pass



del plangParser