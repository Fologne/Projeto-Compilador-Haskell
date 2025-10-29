from antlr4 import *
from HaskellLexer import HaskellLexer
from HaskellParser import HaskellParser
from graphviz import Digraph

def draw_tree(node, parser, graph, parent_id=None, node_id=0):
    if hasattr(node, 'getRuleIndex'):
        label = parser.ruleNames[node.getRuleIndex()]
    else:
        label = node.getText() if hasattr(node, 'getText') else str(node)
    this_id = str(node_id)
    graph.node(this_id, label)
    if parent_id is not None:
        graph.edge(parent_id, this_id)
    next_id = node_id + 1
    if hasattr(node, 'getChildCount'):
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            next_id = draw_tree(child, parser, graph, this_id, next_id)

    return next_id

def main():
    input_stream = FileStream("Exercicio1e2.hs", encoding="utf-8")
    lexer = HaskellLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = HaskellParser(tokens)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    graph = Digraph(comment='Árvore Sintática', format='png')
    draw_tree(tree, parser, graph)
    graph.render('arvore_sintatica', view=True)

if __name__ == "__main__":
    main()