// Generated from /home/vladimir/Desktop/fl-2021-hse-win/solution/DKA.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DKAParser}.
 */
public interface DKAListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DKAParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(DKAParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(DKAParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#statesInit}.
	 * @param ctx the parse tree
	 */
	void enterStatesInit(DKAParser.StatesInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#statesInit}.
	 * @param ctx the parse tree
	 */
	void exitStatesInit(DKAParser.StatesInitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code statesContinue}
	 * labeled alternative in {@link DKAParser#states}.
	 * @param ctx the parse tree
	 */
	void enterStatesContinue(DKAParser.StatesContinueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code statesContinue}
	 * labeled alternative in {@link DKAParser#states}.
	 * @param ctx the parse tree
	 */
	void exitStatesContinue(DKAParser.StatesContinueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code statesStop}
	 * labeled alternative in {@link DKAParser#states}.
	 * @param ctx the parse tree
	 */
	void enterStatesStop(DKAParser.StatesStopContext ctx);
	/**
	 * Exit a parse tree produced by the {@code statesStop}
	 * labeled alternative in {@link DKAParser#states}.
	 * @param ctx the parse tree
	 */
	void exitStatesStop(DKAParser.StatesStopContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#alphaInit}.
	 * @param ctx the parse tree
	 */
	void enterAlphaInit(DKAParser.AlphaInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#alphaInit}.
	 * @param ctx the parse tree
	 */
	void exitAlphaInit(DKAParser.AlphaInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#initialInit}.
	 * @param ctx the parse tree
	 */
	void enterInitialInit(DKAParser.InitialInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#initialInit}.
	 * @param ctx the parse tree
	 */
	void exitInitialInit(DKAParser.InitialInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#initial}.
	 * @param ctx the parse tree
	 */
	void enterInitial(DKAParser.InitialContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#initial}.
	 * @param ctx the parse tree
	 */
	void exitInitial(DKAParser.InitialContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#terminalInit}.
	 * @param ctx the parse tree
	 */
	void enterTerminalInit(DKAParser.TerminalInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#terminalInit}.
	 * @param ctx the parse tree
	 */
	void exitTerminalInit(DKAParser.TerminalInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#transInit}.
	 * @param ctx the parse tree
	 */
	void enterTransInit(DKAParser.TransInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#transInit}.
	 * @param ctx the parse tree
	 */
	void exitTransInit(DKAParser.TransInitContext ctx);
	/**
	 * Enter a parse tree produced by the {@code edgesContinue}
	 * labeled alternative in {@link DKAParser#edges}.
	 * @param ctx the parse tree
	 */
	void enterEdgesContinue(DKAParser.EdgesContinueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code edgesContinue}
	 * labeled alternative in {@link DKAParser#edges}.
	 * @param ctx the parse tree
	 */
	void exitEdgesContinue(DKAParser.EdgesContinueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code edgesStop}
	 * labeled alternative in {@link DKAParser#edges}.
	 * @param ctx the parse tree
	 */
	void enterEdgesStop(DKAParser.EdgesStopContext ctx);
	/**
	 * Exit a parse tree produced by the {@code edgesStop}
	 * labeled alternative in {@link DKAParser#edges}.
	 * @param ctx the parse tree
	 */
	void exitEdgesStop(DKAParser.EdgesStopContext ctx);
	/**
	 * Enter a parse tree produced by {@link DKAParser#edge}.
	 * @param ctx the parse tree
	 */
	void enterEdge(DKAParser.EdgeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DKAParser#edge}.
	 * @param ctx the parse tree
	 */
	void exitEdge(DKAParser.EdgeContext ctx);
}