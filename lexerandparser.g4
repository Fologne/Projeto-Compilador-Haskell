grammar Haskell;

program: 'main' '::' 'IO' '()' 'main' '=' 'do' '{' lista_declaracao* '}' EOF;

lista_declaracao: lista_declaracao declaracao | declaracao;
declaracao: atribuicao | escrita | leitura | se | enquanto;

atribuicao:
      identificador '=' expressao
    | LET identificador ('=' 'read' identificador '::' tipo | '=' expressao)?;

tipo: INT_T | DOUBLE_T;

escrita: 'putStrLn' (STRING ('++' expressao)? | expressao);
leitura: identificador '<-' 'getLine' atribuicao?;
se: 'if' expressao 'then' (declaracao | expressao) 'else' (declaracao | expressao);
enquanto: 'while' expressao 'then' (declaracao | expressao) 'end';

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

inteiro: '-'? INT;
real: '-'? DOUBLE;
identificador: ID;

INT_T: 'INT';
DOUBLE_T: 'DOUBLE';
LET: 'let';

DOUBLE: [0-9]+ '.' [0-9]* | '.' [0-9]+;
INT: [0-9]+;
STRING: '"' ( ~["\\] | '\\' . )* '"';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;