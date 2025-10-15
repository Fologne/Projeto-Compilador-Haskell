grammar Haskell;
program: 'main' '::' 'IO' '()' 'main' '=' 'do' '{' lista_declaracao* '}'  EOF;

lista_declaracao: lista_declaracao declaracao | declaracao;
declaracao: atribuicao | escrita | leitura | se | enquanto;

atribuicao: identificador '=' expressao |
  LET identificador ('=' 'read' identificador '::' INT_T| '=' expressao)?  |
  LET identificador ('=' 'read' identificador '::' DOUBLE_T| '=' expressao)? ;

escrita: 'putStrLn' (STRING ('++' expressao)?| expressao);
leitura: identificador '<-' 'getLine' atribuicao?;
se: 'if' expressao 'then' (declaracao | expressao) 'else' (declaracao | expressao);
lista_identificador: lista_identificador ',' identificador | identificador;



expressao: expressao '+' termo| expressao '-' termo| termo;
fator: '-' fator           
| '(' expressao ')'  
| inteiro                  
| real                     
| identificador;
inteiro: '-'? INT;
real: '-'? DOUBLE;
termo: termo '*' fator| termo '/' fator| termo '>' fator | termo '<' fator | termo '>=' fator |
 termo '<=' fator | termo '==' fator |fator;

identificador: ID;

INT_T: 'INT';
DOUBLE_T: 'DOUBLE';
DOUBLE  : [0-9]+ '.' [0-9]* | '.' [0-9]+;
LET: 'let';
INT    : [0-9]+ ;
STRING : '"' ( ~["\\] | '\\' . )* '"' ;
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
WS     : [ \t\r\n]+ -> skip ;