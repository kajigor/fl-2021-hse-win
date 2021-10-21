# Generated from plang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\7\13\67\n\13\f\13\16\13:\13\13\3\f\3\f\7\f>\n\f\f\f\16")
        buf.write("\fA\13\f\3\r\6\rD\n\r\r\r\16\rE\3\16\6\16I\n\16\r\16\16")
        buf.write("\16J\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\3\2\7\3\2c|\5\2\62;C\\")
        buf.write("c|\3\2C\\\3\2\f\f\4\2\13\13\"\"\2Q\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37")
        buf.write("\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r*\3\2\2\2")
        buf.write("\17,\3\2\2\2\21/\3\2\2\2\23\62\3\2\2\2\25\64\3\2\2\2\27")
        buf.write(";\3\2\2\2\31C\3\2\2\2\33H\3\2\2\2\35\36\7A\2\2\36\4\3")
        buf.write("\2\2\2\37 \7\"\2\2 !\7<\2\2!\"\7/\2\2\"\6\3\2\2\2#$\7")
        buf.write("\60\2\2$\b\3\2\2\2%&\7\"\2\2&\n\3\2\2\2\'(\7\"\2\2()\7")
        buf.write("*\2\2)\f\3\2\2\2*+\7+\2\2+\16\3\2\2\2,-\7.\2\2-.\7\"\2")
        buf.write("\2.\20\3\2\2\2/\60\7=\2\2\60\61\7\"\2\2\61\22\3\2\2\2")
        buf.write("\62\63\7*\2\2\63\24\3\2\2\2\648\t\2\2\2\65\67\t\3\2\2")
        buf.write("\66\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29\26\3")
        buf.write("\2\2\2:8\3\2\2\2;?\t\4\2\2<>\t\3\2\2=<\3\2\2\2>A\3\2\2")
        buf.write("\2?=\3\2\2\2?@\3\2\2\2@\30\3\2\2\2A?\3\2\2\2BD\t\5\2\2")
        buf.write("CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\32\3\2\2\2G")
        buf.write("I\t\6\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3")
        buf.write("\2\2\2LM\b\16\2\2M\34\3\2\2\2\7\28?EJ\3\b\2\2")
        return buf.getvalue()


class plangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    IDENTIFICATOR = 10
    VARIABLE = 11
    NEWLINES = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'?'", "' :-'", "'.'", "' '", "' ('", "')'", "', '", "'; '", 
            "'('" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFICATOR", "VARIABLE", "NEWLINES", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "IDENTIFICATOR", "VARIABLE", "NEWLINES", 
                  "WS" ]

    grammarFileName = "plang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


