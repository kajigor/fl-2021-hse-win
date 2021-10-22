// Generated from /home/stepan/Dropbox/ll/hse/works/fl-2021-hse-win/plang/plang.g4 by ANTLR 4.9.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link plangParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface plangVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link plangParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(plangParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(plangParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#relationship}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelationship(plangParser.RelationshipContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#string}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString(plangParser.StringContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#argument}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgument(plangParser.ArgumentContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtom(plangParser.AtomContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#goal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGoal(plangParser.GoalContext ctx);
	/**
	 * Visit a parse tree produced by {@link plangParser#arithmetic}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArithmetic(plangParser.ArithmeticContext ctx);
}