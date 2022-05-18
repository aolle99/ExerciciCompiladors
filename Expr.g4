grammar Expr;
root : bloc EOF ;
bloc : instr*;

instr : VAR ASSIG expr #VarAssigInstr
      | WRITE expr #WriteInstr
      | IF comparator THEN bloc END #IfInstr
      | WHILE comparator DO bloc END #WhileInstr
      | FUNCTION VAR '(' VAR* ')' bloc END #FunctionInstr
      | MAIN bloc END #MainInstr
      | RETURN expr #ReturnInstr
      ;

expr : VAR '(' param* ')' #CallInstr
     | <assoc=right> expr POW expr #PowExpr
     | expr (MULT | DIV) expr #MultDivExpr
     | expr (MES | MENUS) expr #MesMenExpr
     | (INT | VAR) #TypesExpr
     ;

comparator : expr EQUAL expr
            | expr DIFF expr
            | expr GREATER_EQUAL expr
            | expr LESS_EQUAL expr
            | expr GREATER expr
            | expr LESS expr
            ;

param: expr COMMA
     | expr
     ;

FUNCTION: 'function' ;
RETURN: 'return' ;
MAIN: 'main' ;
COMMA: ',' -> skip;

IF : 'if' ;
THEN : 'then' ;
END : 'end' ;

WHILE : 'while' ;
DO : 'do' ;

WRITE : 'write' ;
ASSIG : ':=' ;

INT : [0-9]+ ;
VAR : [a-zA-Z][a-zA-Z0-9]* ;

MES : '+' ;
MENUS : '-' ;
MULT : '*' ;
DIV : '/' ;
POW : '^' ;

EQUAL : '=' ;
DIFF : '<>' ;
GREATER_EQUAL : '>=';
LESS_EQUAL : '<=';
GREATER : '>';
LESS : '<';
WS : [ \n]+ -> skip ;