grammar plang;
    start : program ;

    program : relationship* '?' goal NEWLINES? ;

    relationship : string+ ;

    string : atom (' :-' goal | '.') NEWLINES ;

    argument : ' ' IDENTIFICATOR
             | ' (' IDENTIFICATOR  argument+ ')'
             | ' ' VARIABLE
             ;

    atom : IDENTIFICATOR  argument* ;

    goal : ' ' arithmetic '.' ;

    arithmetic    : arithmetic ', ' arithmetic
                  | arithmetic '; ' arithmetic
                  | '(' arithmetic ')'
                  | atom
                  ;

    IDENTIFICATOR : [a-z][a-zA-Z0-9]* ;
    VARIABLE      : [A-Z][a-zA-Z0-9]* ;
    NEWLINES      : [\n]+             ;

    WS    : [ \t]+ -> skip ;
