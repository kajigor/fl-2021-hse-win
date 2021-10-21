grammar plang;
    start         : relationships '?' chain    ;

    relationships : relationship* ;

    relationship  : string*                     ;

    string        : atom ':-' arithmetic '.'       ;

    identificator : ('a'..'z')(('a'..'z')|('A'..'Z')|('0'..'9'))* ;

    argument : variable
             | atom
             ;

    variable : ('A'..'Z')(('a'..'z')|('A'..'Z')|('0'..'9'))*;

    atom          : identificator  argument*  ;

    arithmetic :  ;

    WS    : [ \t\r\n]+ -> skip ;
