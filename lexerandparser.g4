grammar Haskell;
program: 'main' '::' 'IO' '()' 'main' '=' 'do' lista_declaracao*  EOF;

lista_declaracao: lista_declaracao declaracao | declaracao;
declaracao: atribuicao | escrita | leitura | se | se_nao | enquanto | faca_enquanto;

atribuicao: identificador '=' expressao |
  LET identificador ('=' 'read' identificador '::' 'INT'| '=' expressao)?  |
  LET identificador ('=' 'read' identificador '::' 'DOUBLE'| '=' expressao)? ;

escrita: 'putStrLn' (STRING | expressao);
leitura: identificador '<-' 'getLine' atribuicao?;
lista_identificador: lista_identificador ',' identificador | identificador;



expressao: expressao '+' termo| expressao '-' termo| termo;
fator: '-' fator           
| '(' expressao ')'  
| inteiro                  
| real                     
| identificador;
inteiro: '-'? INT;
real: '-'? DOUBLE;
termo: termo '*' fator| termo '/' fator| fator;

identificador: ID;

DOUBLE  : [0-9]+ '.' [0-9]* | '.' [0-9]+;
LET: 'let';
INT    : [0-9]+ ;
STRING : '"' ( ~["\\] | '\\' . )* '"' ;
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
WS     : [ \t\r\n]+ -> skip ;