grammar plang;
    start         : program ;

    program : relationship* '?' goal NEWLINES? ;

    relationship  : string+                     ;

    string       : atom (' :-' goal | '.') NEWLINES ;

    //IDENTIFICATOR : ('a'..'z')(ANY*) ;
    //VARIABLE      : ('A'..'Z')(ANY*) ;
    IDENTIFICATOR   : [a-z][a-zA-Z0-9]* ;
    VARIABLE        : [A-Z][a-zA-Z0-9]* ;
    NEWLINES         : [\n]+            ;

    argument : ' ' VARIABLE
             | ' (' VARIABLE ')'
             | ' (' atom ')'
             | ' ' IDENTIFICATOR
             ;

    atom        : IDENTIFICATOR  argument*  ;

    goal : ' ' arithmetic '.' ;

    arithmetic  : arithmetic ', ' arithmetic
                | arithmetic '; ' arithmetic
                | '(' arithmetic ')'
                | atom
                ;

    //WS    : [\t]+ -> skip ;
