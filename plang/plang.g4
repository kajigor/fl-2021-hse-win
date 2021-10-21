grammar plang;
    start         : program ;

    program : relationship* '?' goal NEWLINES? ;

    relationship  : string+                     ;

    string        : atom ' :-' goal NEWLINES
                  | atom '.' NEWLINES
                  ;

    ANY : (('a'..'z')|('A'..'Z')|('0'..'9')) ;
    IDENTIFICATOR : ('a'..'z')ANY* ;
    VARIABLE      : ('A'..'Z')ANY* ;
    NEWLINES      : [\n]+          ;

    argument : ' (' atom ')'
             | ' ' VARIABLE
             ;

    atom        : IDENTIFICATOR  argument*  ;

    goal : ' ' arithmetic '.' ;

    arithmetic  : left=arithmetic op=',' right=arithmetic #opExpr
                | left=arithmetic op=';' right=arithmetic #opExpr
                | '(' arithmetic ')'                      #parentExpr
                | single=atom                             #atomExpr
                ;

    //WS    : [\t]+ -> skip ;
