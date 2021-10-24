// Generated from /home/vladimir/Desktop/fl-2021-hse-win/solution/DKA.g4 by ANTLR 4.9.1

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DKAParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, SYMB=9, 
		NEWLINE=10, WS=11;
	public static final int
		RULE_start = 0, RULE_statesInit = 1, RULE_states = 2, RULE_alphaInit = 3, 
		RULE_initialInit = 4, RULE_initial = 5, RULE_terminalInit = 6, RULE_transInit = 7, 
		RULE_edges = 8, RULE_edge = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "statesInit", "states", "alphaInit", "initialInit", "initial", 
			"terminalInit", "transInit", "edges", "edge"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'states=['", "']'", "','", "'alpha=['", "'initial=['", "'accepting=['", 
			"'trans=['", "'>'", null, "'\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "SYMB", "NEWLINE", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "DKA.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DKAParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public StatesInitContext statesInit() {
			return getRuleContext(StatesInitContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(DKAParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(DKAParser.NEWLINE, i);
		}
		public AlphaInitContext alphaInit() {
			return getRuleContext(AlphaInitContext.class,0);
		}
		public InitialInitContext initialInit() {
			return getRuleContext(InitialInitContext.class,0);
		}
		public TerminalInitContext terminalInit() {
			return getRuleContext(TerminalInitContext.class,0);
		}
		public TransInitContext transInit() {
			return getRuleContext(TransInitContext.class,0);
		}
		public TerminalNode EOF() { return getToken(DKAParser.EOF, 0); }
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitStart(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitStart(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			statesInit();
			setState(21);
			match(NEWLINE);
			setState(22);
			alphaInit();
			setState(23);
			match(NEWLINE);
			setState(24);
			initialInit();
			setState(25);
			match(NEWLINE);
			setState(26);
			terminalInit();
			setState(27);
			match(NEWLINE);
			setState(28);
			transInit();
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(29);
				match(NEWLINE);
				}
				}
				setState(34);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(35);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatesInitContext extends ParserRuleContext {
		public StatesContext states() {
			return getRuleContext(StatesContext.class,0);
		}
		public StatesInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statesInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterStatesInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitStatesInit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitStatesInit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatesInitContext statesInit() throws RecognitionException {
		StatesInitContext _localctx = new StatesInitContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statesInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			match(T__0);
			setState(38);
			states();
			setState(39);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatesContext extends ParserRuleContext {
		public StatesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_states; }
	 
		public StatesContext() { }
		public void copyFrom(StatesContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StatesContinueContext extends StatesContext {
		public TerminalNode SYMB() { return getToken(DKAParser.SYMB, 0); }
		public StatesContext states() {
			return getRuleContext(StatesContext.class,0);
		}
		public StatesContinueContext(StatesContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterStatesContinue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitStatesContinue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitStatesContinue(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class StatesStopContext extends StatesContext {
		public TerminalNode SYMB() { return getToken(DKAParser.SYMB, 0); }
		public StatesStopContext(StatesContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterStatesStop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitStatesStop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitStatesStop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatesContext states() throws RecognitionException {
		StatesContext _localctx = new StatesContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_states);
		try {
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new StatesContinueContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(41);
				match(SYMB);
				setState(42);
				match(T__2);
				setState(43);
				states();
				}
				break;
			case 2:
				_localctx = new StatesStopContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(44);
				match(SYMB);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AlphaInitContext extends ParserRuleContext {
		public StatesContext states() {
			return getRuleContext(StatesContext.class,0);
		}
		public AlphaInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_alphaInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterAlphaInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitAlphaInit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitAlphaInit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AlphaInitContext alphaInit() throws RecognitionException {
		AlphaInitContext _localctx = new AlphaInitContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_alphaInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(T__3);
			setState(48);
			states();
			setState(49);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitialInitContext extends ParserRuleContext {
		public InitialContext initial() {
			return getRuleContext(InitialContext.class,0);
		}
		public InitialInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initialInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterInitialInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitInitialInit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitInitialInit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InitialInitContext initialInit() throws RecognitionException {
		InitialInitContext _localctx = new InitialInitContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_initialInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(T__4);
			setState(52);
			initial();
			setState(53);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitialContext extends ParserRuleContext {
		public TerminalNode SYMB() { return getToken(DKAParser.SYMB, 0); }
		public InitialContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initial; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterInitial(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitInitial(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitInitial(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InitialContext initial() throws RecognitionException {
		InitialContext _localctx = new InitialContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_initial);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			match(SYMB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminalInitContext extends ParserRuleContext {
		public StatesContext states() {
			return getRuleContext(StatesContext.class,0);
		}
		public TerminalInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terminalInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterTerminalInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitTerminalInit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitTerminalInit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TerminalInitContext terminalInit() throws RecognitionException {
		TerminalInitContext _localctx = new TerminalInitContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_terminalInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(T__5);
			setState(58);
			states();
			setState(59);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TransInitContext extends ParserRuleContext {
		public EdgesContext edges() {
			return getRuleContext(EdgesContext.class,0);
		}
		public TransInitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_transInit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterTransInit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitTransInit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitTransInit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TransInitContext transInit() throws RecognitionException {
		TransInitContext _localctx = new TransInitContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_transInit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(T__6);
			setState(62);
			edges();
			setState(63);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EdgesContext extends ParserRuleContext {
		public EdgesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edges; }
	 
		public EdgesContext() { }
		public void copyFrom(EdgesContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class EdgesContinueContext extends EdgesContext {
		public EdgeContext edge() {
			return getRuleContext(EdgeContext.class,0);
		}
		public EdgesContext edges() {
			return getRuleContext(EdgesContext.class,0);
		}
		public EdgesContinueContext(EdgesContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterEdgesContinue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitEdgesContinue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitEdgesContinue(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class EdgesStopContext extends EdgesContext {
		public EdgeContext edge() {
			return getRuleContext(EdgeContext.class,0);
		}
		public EdgesStopContext(EdgesContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterEdgesStop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitEdgesStop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitEdgesStop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EdgesContext edges() throws RecognitionException {
		EdgesContext _localctx = new EdgesContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_edges);
		try {
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new EdgesContinueContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				edge();
				setState(66);
				match(T__2);
				setState(67);
				edges();
				}
				break;
			case 2:
				_localctx = new EdgesStopContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(69);
				edge();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EdgeContext extends ParserRuleContext {
		public List<TerminalNode> SYMB() { return getTokens(DKAParser.SYMB); }
		public TerminalNode SYMB(int i) {
			return getToken(DKAParser.SYMB, i);
		}
		public EdgeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_edge; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).enterEdge(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof DKAListener ) ((DKAListener)listener).exitEdge(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof DKAVisitor ) return ((DKAVisitor<? extends T>)visitor).visitEdge(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EdgeContext edge() throws RecognitionException {
		EdgeContext _localctx = new EdgeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_edge);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(SYMB);
			setState(73);
			match(T__7);
			setState(74);
			match(SYMB);
			setState(75);
			match(T__7);
			setState(76);
			match(SYMB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\rQ\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2!\n\2\f\2\16\2$\13\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\n"+
		"I\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24"+
		"\2\2\2I\2\26\3\2\2\2\4\'\3\2\2\2\6/\3\2\2\2\b\61\3\2\2\2\n\65\3\2\2\2"+
		"\f9\3\2\2\2\16;\3\2\2\2\20?\3\2\2\2\22H\3\2\2\2\24J\3\2\2\2\26\27\5\4"+
		"\3\2\27\30\7\f\2\2\30\31\5\b\5\2\31\32\7\f\2\2\32\33\5\n\6\2\33\34\7\f"+
		"\2\2\34\35\5\16\b\2\35\36\7\f\2\2\36\"\5\20\t\2\37!\7\f\2\2 \37\3\2\2"+
		"\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\7\2\2\3&\3\3"+
		"\2\2\2\'(\7\3\2\2()\5\6\4\2)*\7\4\2\2*\5\3\2\2\2+,\7\13\2\2,-\7\5\2\2"+
		"-\60\5\6\4\2.\60\7\13\2\2/+\3\2\2\2/.\3\2\2\2\60\7\3\2\2\2\61\62\7\6\2"+
		"\2\62\63\5\6\4\2\63\64\7\4\2\2\64\t\3\2\2\2\65\66\7\7\2\2\66\67\5\f\7"+
		"\2\678\7\4\2\28\13\3\2\2\29:\7\13\2\2:\r\3\2\2\2;<\7\b\2\2<=\5\6\4\2="+
		">\7\4\2\2>\17\3\2\2\2?@\7\t\2\2@A\5\22\n\2AB\7\4\2\2B\21\3\2\2\2CD\5\24"+
		"\13\2DE\7\5\2\2EF\5\22\n\2FI\3\2\2\2GI\5\24\13\2HC\3\2\2\2HG\3\2\2\2I"+
		"\23\3\2\2\2JK\7\13\2\2KL\7\n\2\2LM\7\13\2\2MN\7\n\2\2NO\7\13\2\2O\25\3"+
		"\2\2\2\5\"/H";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}