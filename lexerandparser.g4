grammar Haskell;
program: 'main' '::' 'IO' '()' lista_declaracao*  EOF;
//program: 'main' '=' 'do' 

lista_declaracao: lista_declaracao declaracao | declaracao;
declaracao: atribuicao | leitura | escrita | enquanto | faca_enquanto;

atribuicao: identificador '=' expressao |
 'int' identificador ('=' expressao)? |
  'double' identificador ('=' expressao)?;

identificador: ID;

FLOAT  : [0-9]+ '.' [0-9]*  // 12.  12.34
       | '.' [0-9]+         // .5
       ;
INT    : [0-9]+ ;
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
WS     : [ \t\r\n]+ -> skip ;