# Generated from Haskell.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HaskellParser import HaskellParser
else:
    from HaskellParser import HaskellParser

# This class defines a complete listener for a parse tree produced by HaskellParser.
class HaskellListener(ParseTreeListener):

    # Enter a parse tree produced by HaskellParser#program.
    def enterProgram(self, ctx:HaskellParser.ProgramContext):
        pass

    # Exit a parse tree produced by HaskellParser#program.
    def exitProgram(self, ctx:HaskellParser.ProgramContext):
        pass


    # Enter a parse tree produced by HaskellParser#lista_declaracao.
    def enterLista_declaracao(self, ctx:HaskellParser.Lista_declaracaoContext):
        pass

    # Exit a parse tree produced by HaskellParser#lista_declaracao.
    def exitLista_declaracao(self, ctx:HaskellParser.Lista_declaracaoContext):
        pass


    # Enter a parse tree produced by HaskellParser#declaracao.
    def enterDeclaracao(self, ctx:HaskellParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by HaskellParser#declaracao.
    def exitDeclaracao(self, ctx:HaskellParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by HaskellParser#atribuicao.
    def enterAtribuicao(self, ctx:HaskellParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by HaskellParser#atribuicao.
    def exitAtribuicao(self, ctx:HaskellParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by HaskellParser#tipo.
    def enterTipo(self, ctx:HaskellParser.TipoContext):
        pass

    # Exit a parse tree produced by HaskellParser#tipo.
    def exitTipo(self, ctx:HaskellParser.TipoContext):
        pass


    # Enter a parse tree produced by HaskellParser#escrita.
    def enterEscrita(self, ctx:HaskellParser.EscritaContext):
        pass

    # Exit a parse tree produced by HaskellParser#escrita.
    def exitEscrita(self, ctx:HaskellParser.EscritaContext):
        pass


    # Enter a parse tree produced by HaskellParser#leitura.
    def enterLeitura(self, ctx:HaskellParser.LeituraContext):
        pass

    # Exit a parse tree produced by HaskellParser#leitura.
    def exitLeitura(self, ctx:HaskellParser.LeituraContext):
        pass


    # Enter a parse tree produced by HaskellParser#se.
    def enterSe(self, ctx:HaskellParser.SeContext):
        pass

    # Exit a parse tree produced by HaskellParser#se.
    def exitSe(self, ctx:HaskellParser.SeContext):
        pass


    # Enter a parse tree produced by HaskellParser#enquanto.
    def enterEnquanto(self, ctx:HaskellParser.EnquantoContext):
        pass

    # Exit a parse tree produced by HaskellParser#enquanto.
    def exitEnquanto(self, ctx:HaskellParser.EnquantoContext):
        pass


    # Enter a parse tree produced by HaskellParser#bloco.
    def enterBloco(self, ctx:HaskellParser.BlocoContext):
        pass

    # Exit a parse tree produced by HaskellParser#bloco.
    def exitBloco(self, ctx:HaskellParser.BlocoContext):
        pass


    # Enter a parse tree produced by HaskellParser#expressao.
    def enterExpressao(self, ctx:HaskellParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by HaskellParser#expressao.
    def exitExpressao(self, ctx:HaskellParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by HaskellParser#termo.
    def enterTermo(self, ctx:HaskellParser.TermoContext):
        pass

    # Exit a parse tree produced by HaskellParser#termo.
    def exitTermo(self, ctx:HaskellParser.TermoContext):
        pass


    # Enter a parse tree produced by HaskellParser#fator.
    def enterFator(self, ctx:HaskellParser.FatorContext):
        pass

    # Exit a parse tree produced by HaskellParser#fator.
    def exitFator(self, ctx:HaskellParser.FatorContext):
        pass


    # Enter a parse tree produced by HaskellParser#inteiro.
    def enterInteiro(self, ctx:HaskellParser.InteiroContext):
        pass

    # Exit a parse tree produced by HaskellParser#inteiro.
    def exitInteiro(self, ctx:HaskellParser.InteiroContext):
        pass


    # Enter a parse tree produced by HaskellParser#real.
    def enterReal(self, ctx:HaskellParser.RealContext):
        pass

    # Exit a parse tree produced by HaskellParser#real.
    def exitReal(self, ctx:HaskellParser.RealContext):
        pass


    # Enter a parse tree produced by HaskellParser#identificador.
    def enterIdentificador(self, ctx:HaskellParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by HaskellParser#identificador.
    def exitIdentificador(self, ctx:HaskellParser.IdentificadorContext):
        pass



del HaskellParser