grammar plang;
    start         : program ;

    program : relationships=relationship* '?' final=goal;

    relationship  : string+                     ;

    string        : atom ' :-' goal
                  | atom '.' NEWLINES
                  ;

    ANY : (('a'..'z')|('A'..'Z')|('0'..'9')) ;
    IDENTIFICATOR : ('a'..'z')ANY* ;
    VARIABLE      : ('A'..'Z')ANY* ;
    NEWLINES      : [\n]+          ;

    argument : ' ' VARIABLE
             | ' (' atom ')'
             ;

    atom        : IDENTIFICATOR  argument*  ;

    goal : ' ' arithmetic '.' NEWLINES ;

    arithmetic  : left=arithmetic op=',' right=arithmetic #opExpr
                | left=arithmetic op=';' right=arithmetic #opExpr
                | '(' arithmetic ')'                      #parentExpr
                | single=atom                             #atomExpr
                ;

    //WS    : [\t]+ -> skip ;
