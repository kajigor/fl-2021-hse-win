# Generated from plang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .plangParser import plangParser
else:
    from plangParser import plangParser

# This class defines a complete generic visitor for a parse tree produced by plangParser.

class plangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by plangParser#start.
    def visitStart(self, ctx:plangParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#program.
    def visitProgram(self, ctx:plangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#relationship.
    def visitRelationship(self, ctx:plangParser.RelationshipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#string.
    def visitString(self, ctx:plangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#argument.
    def visitArgument(self, ctx:plangParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#atom.
    def visitAtom(self, ctx:plangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#goal.
    def visitGoal(self, ctx:plangParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#opExpr.
    def visitOpExpr(self, ctx:plangParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#atomExpr.
    def visitAtomExpr(self, ctx:plangParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by plangParser#parentExpr.
    def visitParentExpr(self, ctx:plangParser.ParentExprContext):
        return self.visitChildren(ctx)



del plangParser