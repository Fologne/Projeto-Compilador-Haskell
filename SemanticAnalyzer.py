# SemanticAnalyzer.py
from HaskellVisitor import HaskellVisitor

class SemanticAnalyzer(HaskellVisitor):
    def __init__(self):
        # tabela de símbolos: nome -> tipo (string "int"/"double"/"string"/"Unknown")
        self.symbols = {}
        self.errors = []

    # ---------------- helpers ----------------
    def _error(self, msg):
        self.errors.append(msg)

    def _get_ident_name(self, ident_ctx):
        """
        ident_ctx pode ser:
         - None
         - um único Context com getText()
         - uma lista [Context,...]
        Retorna string ou None.
        """
        if ident_ctx is None:
            return None
        if isinstance(ident_ctx, list):
            if len(ident_ctx) == 0:
                return None
            return ident_ctx[0].getText()
        # geralmente é um ParserRuleContext com getText()
        try:
            return ident_ctx.getText()
        except Exception:
            # fallback: str()
            return str(ident_ctx)

    def _is_let_decl(self, ctx):
        """
        Detecta se a atribuição é um 'let'. Faz checagens robustas:
         - tenta ctx.LET() (padrão ANTLR)
         - ou procura a string 'let' em ctx.getText() (fallback)
        """
        try:
            let_node = ctx.LET()
            if let_node:
                return True
        except Exception:
            pass

        # fallback (menos elegante, mas seguro)
        txt = ""
        try:
            txt = ctx.getText()
        except Exception:
            txt = ""
        # normaliza minusculas para procurar 'let' como token
        return 'let' in txt.lower()

    # ---------------- reporting ----------------
    def report(self):
        if self.errors:
            print("\nERROS SEMÂNTICOS DETECTADOS:")
            for e in self.errors:
                print("  -", e)
            raise SystemExit(1)
        else:
            print("Análise semântica concluída sem erros.")

    # ---------------- visitors principais ----------------
    def visitProgram(self, ctx):
        # percorre lista_declaracao / bloco
        self.visitChildren(ctx)
        # ao concluir, relatar
        self.report()
        return None

    def visitLista_declaracao(self, ctx):
        return self.visitChildren(ctx)

    def visitBloco(self, ctx):
        # bloco possui várias declaracao()
        # evite visitChildren genérico que pode mascarar ordem
        try:
            for d in ctx.declaracao():
                self.visit(d)
        except Exception:
            # fallback
            self.visitChildren(ctx)
        return None

    def visitDeclaracao(self, ctx):
        # delega para visitantes específicos (atribuição, leitura, escrita, etc.)
        return self.visitChildren(ctx)

    # ---------------- leitura ----------------
    def visitLeitura(self, ctx):
        # leitura: identificador '<-' 'getLine'
        ident_ctx = ctx.identificador()
        name = self._get_ident_name(ident_ctx)
        if name is None:
            self._error("Leitura com identificador inválido.")
            return None
        # getLine retorna string
        self.symbols[name] = "string"
        return None

    # ---------------- atribuição / let ----------------
    def visitAtribuicao(self, ctx):
        # obter identificador do lado esquerdo (pode ser list ou único)
        ident_ctx = ctx.identificador()
        name = self._get_ident_name(ident_ctx)

        if name is None:
            self._error("Atribuição com identificador inválido.")
            return None

        # detectar let (declaração) robustamente
        is_let = self._is_let_decl(ctx)

        if is_let:
            # let x = expr  (declara)
            if name in self.symbols:
                self._error(f"Variável '{name}' já foi declarada.")
                # ainda assim visita expressão (para captar usos dentro)
                if ctx.expressao():
                    self.visit(ctx.expressao())
                return None

            # inferir tipo pela expressão (se possível)
            expr = ctx.expressao()
            tipo = "Unknown"
            if expr is not None:
                tipo = self.visit(expr) or "Unknown"
            self.symbols[name] = tipo
            return tipo
        else:
            # atribuição normal x = expr
            if name not in self.symbols:
                self._error(f"Variável '{name}' usada antes de ser declarada.")
                # ainda visitamos a expressão à direita para coletar outros erros
                if ctx.expressao():
                    self.visit(ctx.expressao())
                return None

            # visita SOMENTE a expressão à direita (não visite o identificador da esquerda)
            expr = ctx.expressao()
            expr_tipo = None
            if expr is not None:
                expr_tipo = self.visit(expr)

            # opcional: checar compatibilidade de tipos (quando ambos conhecidos)
            var_tipo = self.symbols.get(name, "Unknown")
            if var_tipo != "Unknown" and expr_tipo is not None and expr_tipo != "Unknown":
                if var_tipo != expr_tipo:
                    self._error(
                        f"Atribuição incompatível: variável '{name}' é '{var_tipo}' mas expressão é '{expr_tipo}'."
                    )

            return var_tipo

    # ---------------- escrita / se / enquanto ----------------
    def visitEscrita(self, ctx):
        # putStrLn STRING ++ expressao  ou putStrLn expressao
        # visitar filhos para detectar uso de ids
        return self.visitChildren(ctx)

    def visitSe(self, ctx):
        return self.visitChildren(ctx)

    def visitEnquanto(self, ctx):
        return self.visitChildren(ctx)

    # ---------------- expressões / termos / fatores ----------------
    def visitExpressao(self, ctx):
        # não tentar inferir tipo complexo aqui; apenas propagar tipos simples:
        # se for literal inteiro/real -> retorna "int"/"double"
        # se envolver operadores -> tenta combinar tipos dos filhos
        # fallback: visita filhos e retorna primeiro tipo conhecido
        result_type = None
        for c in ctx.getChildren():
            try:
                t = c.accept(self)
                if t:
                    # prioriza tipos concretos
                    if result_type is None:
                        result_type = t
                    elif result_type != t:
                        # se houver conflito entre int/double -> promote to double
                        if (result_type == "int" and t == "double") or (result_type == "double" and t == "int"):
                            result_type = "double"
                        else:
                            # conflitos string vs int/double -> Unknown (ou reportar)
                            result_type = result_type
            except Exception:
                pass
        return result_type

    def visitTermo(self, ctx):
        return self.visitChildren(ctx)

    def visitFator(self, ctx):
        # fatores podem ser (expressao), inteiro, real, identificador, STRING, 'read' identificador '::' tipo
        # se for inteiro/real/STRING, as rules abaixo (visitInteiro/visitReal) serão chamadas via visitChildren
        return self.visitChildren(ctx)

    # ---------------- literais e identificador ----------------
    def visitInteiro(self, ctx):
        # inteiro: '-'? INT
        return "int"

    def visitReal(self, ctx):
        return "double"

    def visitIdentificador(self, ctx):
        # ctx pode ser list/único (dependendo de como visitor é chamado)
        try:
            name = ctx.getText()
        except Exception:
            # fallback: se vier uma lista
            if isinstance(ctx, list) and len(ctx) > 0:
                name = ctx[0].getText()
            else:
                name = str(ctx)

        if name not in self.symbols:
            self._error(f"Variável '{name}' usada antes de ser declarada.")
            return None
        return self.symbols.get(name, "Unknown")

    # ---------------- fallback visitChildren ----------------
    def visitChildren(self, node):
        result = None
        # alguns nodes em runtime não têm getChildren; usar try
        try:
            children = node.getChildren()
        except Exception:
            # fallback: nada a visitar
            return None

        for c in children:
            try:
                if hasattr(c, "accept"):
                    r = c.accept(self)
                    if r is not None:
                        result = r if result is None else result
            except Exception:
                # ignore nodes que não aceitam visitor
                pass
        return result
