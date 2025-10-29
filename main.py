from antlr4 import *
from HaskellLexer import HaskellLexer
from HaskellParser import HaskellParser

def main():
    input_stream = FileStream("Exercicio1e2.hs", encoding="utf-8")
    lexer = HaskellLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = HaskellParser(tokens)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()