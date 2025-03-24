from antlr4 import *
from SeqDiagramsLexer import SeqDiagramsLexer
from SeqDiagramsParser import SeqDiagramsParser
from antlr4.tree.Tree import TerminalNodeImpl

def print_tree(tree, parser, indent="", is_last=True):
    if isinstance(tree, TerminalNodeImpl):
        print(indent + ("└── " if is_last else "├── ") + tree.getText())
    else:
        rule_name = parser.ruleNames[tree.getRuleIndex()]
        print(indent + ("└── " if is_last else "├── ") + rule_name)
        new_indent = indent + ("    " if is_last else "│   ")
        children = list(tree.getChildren())
        for i, child in enumerate(children):
            print_tree(child, parser, new_indent, i == len(children) - 1)

def main():
    input_string = """
    sequence SeqDiagram {
        actor User;
        object Order : OrderService;
        User -> Order : placeOrder <<create>>;
    }
    """

    input_stream = InputStream(input_string)

    lexer = SeqDiagramsLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = SeqDiagramsParser(stream)

    tree = parser.sequenceDiagram()

    print_tree(tree, parser)

if __name__ == "__main__":
    main()