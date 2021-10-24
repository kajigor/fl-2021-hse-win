public class Visitor extends DKABaseVisitor<Object> {

    String start;
    String[] _isFinal, _alphabet, _states, _transitions;

    Visitor()
    {

    }

    @Override
    public Object visitStatesInit(DKAParser.StatesInitContext ctx) {
        _states = ctx.states().getText().split(",");
        return super.visitStatesInit(ctx);
    }

    @Override
    public Object visitAlphaInit(DKAParser.AlphaInitContext ctx) {
        _alphabet = ctx.states().getText().split(",");
        return super.visitAlphaInit(ctx);
    }

    @Override
    public Object visitInitialInit(DKAParser.InitialInitContext ctx) {
        start = ctx.initial().getText();
        return super.visitChildren(ctx);
    }

    @Override
    public Object visitTerminalInit(DKAParser.TerminalInitContext ctx) {
        _isFinal = ctx.states().getText().split(",");
        return super.visitTerminalInit(ctx);
    }

    @Override
    public Object visitTransInit(DKAParser.TransInitContext ctx) {
        _transitions = ctx.edges().getText().split(",");
        return super.visitTransInit(ctx);
    }
}
