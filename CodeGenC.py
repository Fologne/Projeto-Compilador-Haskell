from HaskellVisitor import HaskellVisitor
from HaskellParser import HaskellParser

class CodeGenC(HaskellVisitor):
    #inicialização da geração de codigo
    def __init__(self):
        self.output = []
        self.indent_level = 0
        self.variables = {}   # nome -> tipo ("int", "double", "string")

    def emit(self, text):
        self.output.append("    " * self.indent_level + text)

    def get_output(self):
        return "\n".join(self.output)

    # ---------- Helpers ----------
    def _first(self, maybe_list):
        if maybe_list is None:
            return None
        if isinstance(maybe_list, list):
            return maybe_list[0] if len(maybe_list) > 0 else None
        return maybe_list

    def _text(self, maybe_ctx_or_token):
        if maybe_ctx_or_token is None:
            return ""
        node = self._first(maybe_ctx_or_token)
        try:
            return node.getText()
        except Exception:
            return str(node)

    # Normalize an expression string if needed (lightweight)
    def _normalize_expr_text(self, raw):
        if raw is None:
            return "0"
        s = str(raw)
        # keep operators as they are; ensure spacing around some tokens for readability
        s = s.replace("++", " ++ ")
        s = s.replace("&&", " && ")
        s = s.replace("||", " || ")
        # no other translations for now
        return s

    # --------------------------
    # Programa
    # --------------------------
    def visitProgram(self, ctx:HaskellParser.ProgramContext):
        # includes
        self.emit("#include <stdio.h>")
        self.emit("#include <stdlib.h>")
        self.emit("")
        self.emit("int main() {")
        self.indent_level += 1

        # visita a lista de declaracao
        lista = ctx.lista_declaracao()
        if isinstance(lista, list):
            for d in lista:
                self.visit(d)
        elif lista:
            self.visit(lista)

        self.emit("return 0;")
        self.indent_level -= 1
        self.emit("}")
        return self.get_output()

    # --------------------------
    # Lista e Bloco de declarações
    # --------------------------
    def visitLista_declaracao(self, ctx):
        return self.visit(ctx.bloco())

    def visitBloco(self, ctx):
        decls = ctx.declaracao()
        if isinstance(decls, list):
            for d in decls:
                self.visit(d)
        elif decls:
            self.visit(decls)
        return None

    # --------------------------
    # Atribuição de variaveis
    # --------------------------
    def visitAtribuicao(self, ctx):
        # get identifier target
        ident_ctx = self._first(ctx.identificador())
        ident = self._text(ident_ctx)

        raw = ctx.getText()

        # CASE: let x = read y :: Tipo  (explicit read cast)
        if ctx.LET() and 'read' in raw and '::' in raw:
            # parse crude: find 'read' and '::'
            pos_read = raw.find('read') + len('read')
            pos_cast = raw.find('::', pos_read)
            src = raw[pos_read:pos_cast].strip()
            tipo = raw[pos_cast+2:].strip()
            if tipo.startswith('Int'):
                c_type = "int"
                conv = f"atoi({src})"
            else:
                c_type = "double"
                conv = f"atof({src})"

            if ident not in self.variables:
                self.variables[ident] = c_type
                self.emit(f"{c_type} {ident} = {conv};")
            else:
                self.emit(f"{ident} = {conv};")
            return None

        # CASE: let ident :: Tipo  or let ident :: Tipo = expr
        if ctx.LET() and ctx.tipo():
            tipo_ctx = self._first(ctx.tipo())
            tipo = self._text(tipo_ctx)
            c_type = "int" if tipo == "Int" else "double"
            self.variables[ident] = c_type
            expr_ctx = self._first(ctx.expressao())
            if expr_ctx:
                expr_text = self._normalize_expr_text(self._text(expr_ctx))
                # if expression contains read(...) handled above; else use raw text
                self.emit(f"{c_type} {ident} = {expr_text};")
            else:
                self.emit(f"{c_type} {ident};")
            return None

        # CASE: let ident = expr  (infer type)
        if ctx.LET() and ctx.expressao():
            expr_ctx = self._first(ctx.expressao())
            expr_text = self._normalize_expr_text(self._text(expr_ctx))
            # infer type: presence of '.' or atof => double, else int
            inferred = "double" if ('.' in expr_text or 'atof' in expr_text) else "int"
            self.variables[ident] = inferred
            self.emit(f"{inferred} {ident} = {expr_text};")
            return None

        # NORMAL assignment: ident = expr
        expr_ctx = self._first(ctx.expressao())
        expr_text = self._normalize_expr_text(self._text(expr_ctx)) if expr_ctx else "0"
        self.emit(f"{ident} = {expr_text};")
        return None

    # --------------------------
    # Escrita (putStrLn)
    # --------------------------
    def visitEscrita(self, ctx):
        # putStrLn STRING or putStrLn STRING ++ expr handled
        if ctx.STRING():
            # check if there's concatenation '++' in children
            raw = ctx.getText()
            if '++' in raw:
                # crude split: "STRING ++ expr"
                parts = raw.split('++', 1)
                left = parts[0].strip()
                right = parts[1].strip()
                # left is the literal, keep as-is; right evaluate
                right_code = right
                # decide format by heuristics
                if any(ch in right_code for ch in ['.', '/', 'atof']):
                    self.emit(f'printf({left} "%f", (double)({right_code}));')
                else:
                    self.emit(f'printf({left} "%d", (int)({right_code}));')
            else:
                self.emit(f'printf({self._text(ctx.STRING())});')
            return None

        # putStrLn expression
        expr_ctx = self._first(ctx.expressao())
        if not expr_ctx:
            return None

        raw = self._text(expr_ctx)
        # handle concat within expression like valor ++ " "
        if '++' in raw:
            l, r = raw.split('++', 1)
            l = l.strip(); r = r.strip()
            # if r is string literal print with space after value
            if r.startswith('"') and r.endswith('"'):
                # decide format for l
                fmt = "%f" if ('.' in l or 'atof' in l) else "%d"
                # remove extra quotes from r? we'll print r directly as literal after formatted value
                # generate: printf("%d ", (int)(l));
                # ensure r contains the actual spaces e.g. " "
                self.emit(f'printf("{fmt} %s", {l}, {r});' if fmt=="%f" else f'printf("{fmt} %s", (int)({l}), {r});')
                return None

        # default: simple expression print
        expr_text = self._normalize_expr_text(raw)
        if any(token in expr_text for token in ['atof', '.', '/']):
            self.emit(f'printf("%f", (double)({expr_text}));')
        else:
            self.emit(f'printf("%d", (int)({expr_text}));')
        return None

    # --------------------------
    # Leitura (x <- getLine)
    # --------------------------
    def visitLeitura(self, ctx):
        ident = self._text(self._first(ctx.identificador()))

        # Se a variável ainda não foi declarada, declare como string
        if ident not in self.variables:
            self.variables[ident] = "string"
            self.emit(f"char {ident}[128];")

        # Ler uma string via scanf
        self.emit(f'scanf("%127s", {ident});')

        return None


    # --------------------------
    # If / Else (se)
    # --------------------------
    def visitSe(self, ctx):
        cond_raw = self._text(self._first(ctx.expressao()))
        cond = self._normalize_expr_text(cond_raw)

        # quick fix: transform patterns like "a<=0||b" (if produced) won't be perfect,
        # but main grammar uses explicit operators so getText is ok.
        self.emit(f"if ({cond}) {{")
        self.indent_level += 1
        # then-block is the bloco after then
        blocos = ctx.bloco()
        if isinstance(blocos, list):
            if len(blocos) >= 1:
                self.visit(blocos[0])
        else:
            if blocos:
                self.visit(blocos)
        self.indent_level -= 1
        self.emit("}")

        # else part: can be 'else se' or 'else bloco'
        if ctx.se():
            self.emit("else ")
            self.visit(ctx.se())
        else:
            # check second bloco child
            if isinstance(blocos, list) and len(blocos) >= 2:
                self.emit("else {")
                self.indent_level += 1
                self.visit(blocos[1])
                self.indent_level -= 1
                self.emit("}")
        return None

    # --------------------------
    # While (enquanto)
    # --------------------------
    def visitEnquanto(self, ctx):
        cond_raw = self._text(self._first(ctx.expressao()))
        cond = self._normalize_expr_text(cond_raw)
        self.emit(f"while ({cond}) {{")
        self.indent_level += 1
        bloco = self._first(ctx.bloco())
        if bloco:
            self.visit(bloco)
        self.indent_level -= 1
        self.emit("}")
        return None

    # --------------------------
    # Expressões / Termos / Fatores (fallbacks simples usando getText)
    # --------------------------
    def visitExpressao(self, ctx):
        # fallback: return the textual representation (preserves tokens/order)
        return self._normalize_expr_text(self._text(ctx))

    def visitTermo(self, ctx):
        return self._normalize_expr_text(self._text(ctx))

    def visitFator(self, ctx):
        # if it's a nested expression, return it parenthesized
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return "(" + self._normalize_expr_text(self._text(ctx.expressao())) + ")"

        # integers, reals, identifiers, strings, read cast
        if ctx.inteiro():
            return self._text(ctx.inteiro())
        if ctx.real():
            return self._text(ctx.real())
        if ctx.identificador():
            return self._text(self._first(ctx.identificador()))
        if ctx.STRING():
            return self._text(ctx.STRING())

        # read ident :: Tipo inside fator
        if ctx.getChildCount() >= 1 and ctx.getChild(0).getText() == 'read':
            ident = self._text(self._first(ctx.identificador()))
            tipo_ctx = self._first(ctx.tipo())
            tipo = self._text(tipo_ctx) if tipo_ctx else "Int"
            if tipo == "Int":
                return f"atoi({ident})"
            else:
                return f"atof({ident})"

        # unary minus handling
        if ctx.getChildCount() >= 2 and ctx.getChild(0).getText() == '-':
            inner = self._first(ctx.fator())
            return "-" + self._normalize_expr_text(self._text(inner))

        # fallback to text
        return self._normalize_expr_text(self._text(ctx))