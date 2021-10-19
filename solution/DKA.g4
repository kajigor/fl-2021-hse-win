grammar DKA;
    start : statesInit NEWLINE alphaInit NEWLINE initialInit NEWLINE terminalInit NEWLINE transInit ;

    statesInit : STATE_KEYWORD states CLOSE ;
    states : STATE COMMA states #statesContinue
           | STATE            #statesStop
           ;

    alphaInit : 'alpha=[' alphabet ',' ;
    alphabet : ALPHA ',' alphabet
             | ALPHA
             ;

    initialInit : INITIAL_KEYWORD initial CLOSE ;
    initial : STATE ;

    terminalInit : TERMINAL_KEYWORD states CLOSE ;

    transInit : TRANS_KEYWORD edges CLOSE ;
    edges : edge COMMA edges #edgesContinue
          | edge           #edgesStop
          ;
    edge : STATE ARROW ALPHA ARROW STATE ;

    STATE_KEYWORD : 'states=[' ;
    ALPHA_KEYWORD : 'alpha=[' ;
    INITIAL_KEYWORD : 'initial=[' ;
    TERMINAL_KEYWORD : 'terminal=[' ;
    TRANS_KEYWORD : 'trans=[' ;
    CLOSE : ']' ;
    COMMA : ',' ;
    ARROW : '>' ;

    STATE : (('a'..'z')|('A'..'Z')|('0'..'9')|'_')+ ;
    ALPHA : (('a'..'z')|('A'..'Z')|('0'..'9')|'_')+ ;
    NEWLINE : '\n' ;

    WS    : [ \t\r]+ -> skip ;