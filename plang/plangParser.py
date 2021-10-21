# Generated from plang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\6\4!\n\4\r\4\16\4\"\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5.\n\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6\66\n\6\3\7\3\7\7\7:\n\7\f\7\16\7=\13\7\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\tI\n\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\7\tQ\n\t\f\t\16\tT\13\t\3\t\2\3\20")
        buf.write("\n\2\4\6\b\n\f\16\20\2\2\2V\2\22\3\2\2\2\4\27\3\2\2\2")
        buf.write("\6 \3\2\2\2\b-\3\2\2\2\n\65\3\2\2\2\f\67\3\2\2\2\16>\3")
        buf.write("\2\2\2\20H\3\2\2\2\22\23\5\4\3\2\23\3\3\2\2\2\24\26\5")
        buf.write("\6\4\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\7\3\2\2\33")
        buf.write("\35\5\16\b\2\34\36\7\17\2\2\35\34\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\5\3\2\2\2\37!\5\b\5\2 \37\3\2\2\2!\"\3\2\2\2\" ")
        buf.write("\3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$%\5\f\7\2%&\7\4\2\2&\'")
        buf.write("\5\16\b\2\'(\7\17\2\2(.\3\2\2\2)*\5\f\7\2*+\7\5\2\2+,")
        buf.write("\7\17\2\2,.\3\2\2\2-$\3\2\2\2-)\3\2\2\2.\t\3\2\2\2/\60")
        buf.write("\7\6\2\2\60\66\7\16\2\2\61\62\7\7\2\2\62\63\5\f\7\2\63")
        buf.write("\64\7\b\2\2\64\66\3\2\2\2\65/\3\2\2\2\65\61\3\2\2\2\66")
        buf.write("\13\3\2\2\2\67;\7\r\2\28:\5\n\6\298\3\2\2\2:=\3\2\2\2")
        buf.write(";9\3\2\2\2;<\3\2\2\2<\r\3\2\2\2=;\3\2\2\2>?\7\6\2\2?@")
        buf.write("\5\20\t\2@A\7\5\2\2A\17\3\2\2\2BC\b\t\1\2CD\7\13\2\2D")
        buf.write("E\5\20\t\2EF\7\b\2\2FI\3\2\2\2GI\5\f\7\2HB\3\2\2\2HG\3")
        buf.write("\2\2\2IR\3\2\2\2JK\f\6\2\2KL\7\t\2\2LQ\5\20\t\7MN\f\5")
        buf.write("\2\2NO\7\n\2\2OQ\5\20\t\6PJ\3\2\2\2PM\3\2\2\2QT\3\2\2")
        buf.write("\2RP\3\2\2\2RS\3\2\2\2S\21\3\2\2\2TR\3\2\2\2\13\27\35")
        buf.write("\"-\65;HPR")
        return buf.getvalue()


class plangParser ( Parser ):

    grammarFileName = "plang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "' :-'", "'.'", "' '", "' ('", 
                     "')'", "','", "';'", "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ANY", "IDENTIFICATOR", 
                      "VARIABLE", "NEWLINES" ]

    RULE_start = 0
    RULE_program = 1
    RULE_relationship = 2
    RULE_string = 3
    RULE_argument = 4
    RULE_atom = 5
    RULE_goal = 6
    RULE_arithmetic = 7

    ruleNames =  [ "start", "program", "relationship", "string", "argument", 
                   "atom", "goal", "arithmetic" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ANY=10
    IDENTIFICATOR=11
    VARIABLE=12
    NEWLINES=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(plangParser.ProgramContext,0)


        def getRuleIndex(self):
            return plangParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = plangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.program()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def goal(self):
            return self.getTypedRuleContext(plangParser.GoalContext,0)


        def relationship(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(plangParser.RelationshipContext)
            else:
                return self.getTypedRuleContext(plangParser.RelationshipContext,i)


        def NEWLINES(self):
            return self.getToken(plangParser.NEWLINES, 0)

        def getRuleIndex(self):
            return plangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = plangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==plangParser.IDENTIFICATOR:
                self.state = 18
                self.relationship()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(plangParser.T__0)
            self.state = 25
            self.goal()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==plangParser.NEWLINES:
                self.state = 26
                self.match(plangParser.NEWLINES)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationshipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(plangParser.StringContext)
            else:
                return self.getTypedRuleContext(plangParser.StringContext,i)


        def getRuleIndex(self):
            return plangParser.RULE_relationship

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationship" ):
                listener.enterRelationship(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationship" ):
                listener.exitRelationship(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationship" ):
                return visitor.visitRelationship(self)
            else:
                return visitor.visitChildren(self)




    def relationship(self):

        localctx = plangParser.RelationshipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_relationship)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 29
                    self.string()

                else:
                    raise NoViableAltException(self)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(plangParser.AtomContext,0)


        def goal(self):
            return self.getTypedRuleContext(plangParser.GoalContext,0)


        def NEWLINES(self):
            return self.getToken(plangParser.NEWLINES, 0)

        def getRuleIndex(self):
            return plangParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = plangParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_string)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.atom()
                self.state = 35
                self.match(plangParser.T__1)
                self.state = 36
                self.goal()
                self.state = 37
                self.match(plangParser.NEWLINES)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.atom()
                self.state = 40
                self.match(plangParser.T__2)
                self.state = 41
                self.match(plangParser.NEWLINES)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(plangParser.VARIABLE, 0)

        def atom(self):
            return self.getTypedRuleContext(plangParser.AtomContext,0)


        def getRuleIndex(self):
            return plangParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = plangParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [plangParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(plangParser.T__3)
                self.state = 46
                self.match(plangParser.VARIABLE)
                pass
            elif token in [plangParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(plangParser.T__4)
                self.state = 48
                self.atom()
                self.state = 49
                self.match(plangParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFICATOR(self):
            return self.getToken(plangParser.IDENTIFICATOR, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(plangParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(plangParser.ArgumentContext,i)


        def getRuleIndex(self):
            return plangParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = plangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(plangParser.IDENTIFICATOR)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    self.argument() 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self):
            return self.getTypedRuleContext(plangParser.ArithmeticContext,0)


        def getRuleIndex(self):
            return plangParser.RULE_goal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoal" ):
                listener.enterGoal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoal" ):
                listener.exitGoal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoal" ):
                return visitor.visitGoal(self)
            else:
                return visitor.visitChildren(self)




    def goal(self):

        localctx = plangParser.GoalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_goal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(plangParser.T__3)
            self.state = 61
            self.arithmetic(0)
            self.state = 62
            self.match(plangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return plangParser.RULE_arithmetic

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OpExprContext(ArithmeticContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a plangParser.ArithmeticContext
            super().__init__(parser)
            self.left = None # ArithmeticContext
            self.op = None # Token
            self.right = None # ArithmeticContext
            self.copyFrom(ctx)

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(plangParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(plangParser.ArithmeticContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpExpr" ):
                listener.enterOpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpExpr" ):
                listener.exitOpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpExpr" ):
                return visitor.visitOpExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ArithmeticContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a plangParser.ArithmeticContext
            super().__init__(parser)
            self.single = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(plangParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParentExprContext(ArithmeticContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a plangParser.ArithmeticContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arithmetic(self):
            return self.getTypedRuleContext(plangParser.ArithmeticContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentExpr" ):
                listener.enterParentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentExpr" ):
                listener.exitParentExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentExpr" ):
                return visitor.visitParentExpr(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = plangParser.ArithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [plangParser.T__8]:
                localctx = plangParser.ParentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 65
                self.match(plangParser.T__8)
                self.state = 66
                self.arithmetic(0)
                self.state = 67
                self.match(plangParser.T__5)
                pass
            elif token in [plangParser.IDENTIFICATOR]:
                localctx = plangParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                localctx.single = self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = plangParser.OpExprContext(self, plangParser.ArithmeticContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        localctx.op = self.match(plangParser.T__6)
                        self.state = 74
                        localctx.right = self.arithmetic(5)
                        pass

                    elif la_ == 2:
                        localctx = plangParser.OpExprContext(self, plangParser.ArithmeticContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        localctx.op = self.match(plangParser.T__7)
                        self.state = 77
                        localctx.right = self.arithmetic(4)
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.arithmetic_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_sempred(self, localctx:ArithmeticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




