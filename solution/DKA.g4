grammar DKA;
    start : statesInit NEWLINE alphaInit NEWLINE initialInit NEWLINE terminalInit NEWLINE transInit '\n'* EOF ;

    statesInit : 'states=[' states ']' ;
    states : SYMB ',' states #statesContinue
           | SYMB            #statesStop
           ;

    alphaInit : 'alpha=[' states ']' ;

    initialInit : 'initial=[' initial ']' ;
    initial : SYMB ;

    terminalInit : 'accepting=[' states ']' ;

    transInit : 'trans=[' edges ']' ;
    edges : edge ',' edges #edgesContinue
          | edge           #edgesStop
          ;
    edge : SYMB '>' SYMB '>' SYMB ;


    SYMB : (('a'..'z')|('A'..'Z')|('0'..'9')|'_')+ ;
    NEWLINE : '\n' ;

    WS    : [ \t\r]+ -> skip ;