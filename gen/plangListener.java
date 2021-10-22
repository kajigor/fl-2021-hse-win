// Generated from /home/stepan/Dropbox/ll/hse/works/fl-2021-hse-win/plang/plang.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link plangParser}.
 */
public interface plangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link plangParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(plangParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(plangParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(plangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(plangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#relationship}.
	 * @param ctx the parse tree
	 */
	void enterRelationship(plangParser.RelationshipContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#relationship}.
	 * @param ctx the parse tree
	 */
	void exitRelationship(plangParser.RelationshipContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(plangParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(plangParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(plangParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(plangParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(plangParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(plangParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#goal}.
	 * @param ctx the parse tree
	 */
	void enterGoal(plangParser.GoalContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#goal}.
	 * @param ctx the parse tree
	 */
	void exitGoal(plangParser.GoalContext ctx);
	/**
	 * Enter a parse tree produced by {@link plangParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic(plangParser.ArithmeticContext ctx);
	/**
	 * Exit a parse tree produced by {@link plangParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic(plangParser.ArithmeticContext ctx);
}