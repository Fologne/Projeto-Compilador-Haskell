grammar Haskell;
//declaracao do programa
program: 'main' '::' 'IO' '()' 'main' '=' 'do' '{' lista_declaracao* '}' EOF;

//lista de declaracoes do programa
lista_declaracao: bloco;
declaracao: atribuicao | escrita | leitura | se | enquanto | declaracao_let;

//atribuicao de tipos inteiro e double
atribuicao:
      identificador '=' expressao
    | LET identificador ('=' 'read' identificador '::' tipo | '=' expressao)?;
tipo: INT_T | DOUBLE_T;
declaracao_let: 'let' identificador ('=' 'read' identificador '::' tipo | '=' expressao);


//declaracao do sistema de escrita, leitura, se e senao e enquanto
escrita: 'putStrLn' (STRING ('++' expressao)? | expressao);
leitura: identificador '<-' 'getLine' atribuicao?;
se: 'if' expressao 'then' bloco ('else' (se | bloco));
enquanto: 'while' expressao 'do' bloco 'end';
bloco: declaracao+;

//operadores logicos
expressao:
      expressao '||' expressao
    | expressao '&&' expressao
    | '!' expressao
    | expressao '==' expressao
    | expressao '!=' expressao
    | expressao '>' expressao
    | expressao '<' expressao
    | expressao '>=' expressao
    | expressao '<=' expressao
    | expressao '+' termo
    | expressao '-' termo
    | termo;


//declaracao dos termos e fatores
termo:
      termo '*' fator
    | termo '/' fator
    | fator;
fator:
      '(' expressao ')'
    | '-' fator
    | inteiro
    | real
    | identificador;

//declaracao do tipo int double e o identificador
inteiro: '-'? INT;
real: '-'? DOUBLE;
identificador: ID;

//tokens lexer
INT_T: 'Int';
DOUBLE_T: 'Double';
LET: 'let';

DOUBLE: [0-9]+ '.' [0-9]* | '.' [0-9]+;
INT: [0-9]+;
STRING: '"' ( ~["\\] | '\\' . )* '"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;