// Generated from /home/vladimir/Desktop/fl-2021-hse-win/solution/DKA.g4 by ANTLR 4.9.1

import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link DKAParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface DKAVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link DKAParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(DKAParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#statesInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatesInit(DKAParser.StatesInitContext ctx);
	/**
	 * Visit a parse tree produced by the {@code statesContinue}
	 * labeled alternative in {@link DKAParser#states}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatesContinue(DKAParser.StatesContinueContext ctx);
	/**
	 * Visit a parse tree produced by the {@code statesStop}
	 * labeled alternative in {@link DKAParser#states}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatesStop(DKAParser.StatesStopContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#alphaInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAlphaInit(DKAParser.AlphaInitContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#initialInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInitialInit(DKAParser.InitialInitContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#initial}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInitial(DKAParser.InitialContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#terminalInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerminalInit(DKAParser.TerminalInitContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#transInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTransInit(DKAParser.TransInitContext ctx);
	/**
	 * Visit a parse tree produced by the {@code edgesContinue}
	 * labeled alternative in {@link DKAParser#edges}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEdgesContinue(DKAParser.EdgesContinueContext ctx);
	/**
	 * Visit a parse tree produced by the {@code edgesStop}
	 * labeled alternative in {@link DKAParser#edges}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEdgesStop(DKAParser.EdgesStopContext ctx);
	/**
	 * Visit a parse tree produced by {@link DKAParser#edge}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEdge(DKAParser.EdgeContext ctx);
}