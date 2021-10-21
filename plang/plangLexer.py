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
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\5\13\64\n\13")
        buf.write("\3\f\3\f\7\f8\n\f\f\f\16\f;\13\f\3\r\3\r\7\r?\n\r\f\r")
        buf.write("\16\rB\13\r\3\16\6\16E\n\16\r\16\16\16F\2\2\17\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\3\2\4\5\2\62;C\\c|\3\2\f\f\2J\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2")
        buf.write("\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r*\3\2\2\2\17")
        buf.write(",\3\2\2\2\21.\3\2\2\2\23\60\3\2\2\2\25\63\3\2\2\2\27\65")
        buf.write("\3\2\2\2\31<\3\2\2\2\33D\3\2\2\2\35\36\7A\2\2\36\4\3\2")
        buf.write("\2\2\37 \7\"\2\2 !\7<\2\2!\"\7/\2\2\"\6\3\2\2\2#$\7\60")
        buf.write("\2\2$\b\3\2\2\2%&\7\"\2\2&\n\3\2\2\2\'(\7\"\2\2()\7*\2")
        buf.write("\2)\f\3\2\2\2*+\7+\2\2+\16\3\2\2\2,-\7.\2\2-\20\3\2\2")
        buf.write("\2./\7=\2\2/\22\3\2\2\2\60\61\7*\2\2\61\24\3\2\2\2\62")
        buf.write("\64\t\2\2\2\63\62\3\2\2\2\64\26\3\2\2\2\659\4c|\2\668")
        buf.write("\5\25\13\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2")
        buf.write("\2:\30\3\2\2\2;9\3\2\2\2<@\4C\\\2=?\5\25\13\2>=\3\2\2")
        buf.write("\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\32\3\2\2\2B@\3\2\2\2")
        buf.write("CE\t\3\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\34")
        buf.write("\3\2\2\2\7\2\639@F\2")
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
    ANY = 10
    IDENTIFICATOR = 11
    VARIABLE = 12
    NEWLINES = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'?'", "' :-'", "'.'", "' '", "' ('", "')'", "','", "';'", "'('" ]

    symbolicNames = [ "<INVALID>",
            "ANY", "IDENTIFICATOR", "VARIABLE", "NEWLINES" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "ANY", "IDENTIFICATOR", "VARIABLE", "NEWLINES" ]

    grammarFileName = "plang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


