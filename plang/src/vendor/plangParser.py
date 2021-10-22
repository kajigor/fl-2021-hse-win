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
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\6\4!\n\4\r\4\16\4\"\3\5\3\5")
        buf.write("\3\5\3\5\5\5)\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\6\6\62\n")
        buf.write("\6\r\6\16\6\63\3\6\3\6\3\6\3\6\5\6:\n\6\3\7\3\7\7\7>\n")
        buf.write("\7\f\7\16\7A\13\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\tM\n\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tU\n\t\f\t\16")
        buf.write("\tX\13\t\3\t\2\3\20\n\2\4\6\b\n\f\16\20\2\2\2\\\2\22\3")
        buf.write("\2\2\2\4\27\3\2\2\2\6 \3\2\2\2\b$\3\2\2\2\n9\3\2\2\2\f")
        buf.write(";\3\2\2\2\16B\3\2\2\2\20L\3\2\2\2\22\23\5\4\3\2\23\3\3")
        buf.write("\2\2\2\24\26\5\6\4\2\25\24\3\2\2\2\26\31\3\2\2\2\27\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32")
        buf.write("\33\7\3\2\2\33\35\5\16\b\2\34\36\7\16\2\2\35\34\3\2\2")
        buf.write("\2\35\36\3\2\2\2\36\5\3\2\2\2\37!\5\b\5\2 \37\3\2\2\2")
        buf.write("!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\7\3\2\2\2$(\5\f\7\2")
        buf.write("%&\7\4\2\2&)\5\16\b\2\')\7\5\2\2(%\3\2\2\2(\'\3\2\2\2")
        buf.write(")*\3\2\2\2*+\7\16\2\2+\t\3\2\2\2,-\7\6\2\2-:\7\f\2\2.")
        buf.write("/\7\7\2\2/\61\7\f\2\2\60\62\5\n\6\2\61\60\3\2\2\2\62\63")
        buf.write("\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\66\7\b\2\2\66:\3\2\2\2\678\7\6\2\28:\7\r\2\29,\3\2\2")
        buf.write("\29.\3\2\2\29\67\3\2\2\2:\13\3\2\2\2;?\7\f\2\2<>\5\n\6")
        buf.write("\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\r\3\2\2\2")
        buf.write("A?\3\2\2\2BC\7\6\2\2CD\5\20\t\2DE\7\5\2\2E\17\3\2\2\2")
        buf.write("FG\b\t\1\2GH\7\13\2\2HI\5\20\t\2IJ\7\b\2\2JM\3\2\2\2K")
        buf.write("M\5\f\7\2LF\3\2\2\2LK\3\2\2\2MV\3\2\2\2NO\f\6\2\2OP\7")
        buf.write("\t\2\2PU\5\20\t\7QR\f\5\2\2RS\7\n\2\2SU\5\20\t\6TN\3\2")
        buf.write("\2\2TQ\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\21\3\2\2")
        buf.write("\2XV\3\2\2\2\f\27\35\"(\639?LTV")
        return buf.getvalue()


class plangParser ( Parser ):

    grammarFileName = "plang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'?'", "' :-'", "'.'", "' '", "' ('", 
                     "')'", "', '", "'; '", "'('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFICATOR", "VARIABLE", 
                      "NEWLINES", "WS" ]

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
    IDENTIFICATOR=10
    VARIABLE=11
    NEWLINES=12
    WS=13

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


        def NEWLINES(self):
            return self.getToken(plangParser.NEWLINES, 0)

        def goal(self):
            return self.getTypedRuleContext(plangParser.GoalContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.atom()
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [plangParser.T__1]:
                self.state = 35
                self.match(plangParser.T__1)
                self.state = 36
                self.goal()
                pass
            elif token in [plangParser.T__2]:
                self.state = 37
                self.match(plangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 40
            self.match(plangParser.NEWLINES)
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

        def IDENTIFICATOR(self):
            return self.getToken(plangParser.IDENTIFICATOR, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(plangParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(plangParser.ArgumentContext,i)


        def VARIABLE(self):
            return self.getToken(plangParser.VARIABLE, 0)

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
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(plangParser.T__3)
                self.state = 43
                self.match(plangParser.IDENTIFICATOR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(plangParser.T__4)
                self.state = 45
                self.match(plangParser.IDENTIFICATOR)
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 46
                    self.argument()
                    self.state = 49 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==plangParser.T__3 or _la==plangParser.T__4):
                        break

                self.state = 51
                self.match(plangParser.T__5)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.match(plangParser.T__3)
                self.state = 54
                self.match(plangParser.VARIABLE)
                pass


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
            self.state = 57
            self.match(plangParser.IDENTIFICATOR)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 58
                    self.argument() 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.state = 64
            self.match(plangParser.T__3)
            self.state = 65
            self.arithmetic(0)
            self.state = 66
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

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(plangParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(plangParser.ArithmeticContext,i)


        def atom(self):
            return self.getTypedRuleContext(plangParser.AtomContext,0)


        def getRuleIndex(self):
            return plangParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [plangParser.T__8]:
                self.state = 69
                self.match(plangParser.T__8)
                self.state = 70
                self.arithmetic(0)
                self.state = 71
                self.match(plangParser.T__5)
                pass
            elif token in [plangParser.IDENTIFICATOR]:
                self.state = 73
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 82
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = plangParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 76
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 77
                        self.match(plangParser.T__6)
                        self.state = 78
                        self.arithmetic(5)
                        pass

                    elif la_ == 2:
                        localctx = plangParser.ArithmeticContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                        self.state = 79
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 80
                        self.match(plangParser.T__7)
                        self.state = 81
                        self.arithmetic(4)
                        pass

             
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
         




