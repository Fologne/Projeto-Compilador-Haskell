# Generated from Haskell.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HaskellParser import HaskellParser
else:
    from HaskellParser import HaskellParser

# This class defines a complete generic visitor for a parse tree produced by HaskellParser.

class HaskellVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HaskellParser#program.
    def visitProgram(self, ctx:HaskellParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#lista_declaracao.
    def visitLista_declaracao(self, ctx:HaskellParser.Lista_declaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#declaracao.
    def visitDeclaracao(self, ctx:HaskellParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#atribuicao.
    def visitAtribuicao(self, ctx:HaskellParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#tipo.
    def visitTipo(self, ctx:HaskellParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#escrita.
    def visitEscrita(self, ctx:HaskellParser.EscritaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#leitura.
    def visitLeitura(self, ctx:HaskellParser.LeituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#se.
    def visitSe(self, ctx:HaskellParser.SeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#enquanto.
    def visitEnquanto(self, ctx:HaskellParser.EnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#bloco.
    def visitBloco(self, ctx:HaskellParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#expressao.
    def visitExpressao(self, ctx:HaskellParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#termo.
    def visitTermo(self, ctx:HaskellParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#fator.
    def visitFator(self, ctx:HaskellParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#inteiro.
    def visitInteiro(self, ctx:HaskellParser.InteiroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#real.
    def visitReal(self, ctx:HaskellParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HaskellParser#identificador.
    def visitIdentificador(self, ctx:HaskellParser.IdentificadorContext):
        return self.visitChildren(ctx)



del HaskellParser