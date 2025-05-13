from antlr4 import *
from SeqDiagramsLexer import SeqDiagramsLexer
from SeqDiagramsParser import SeqDiagramsParser
from antlr4.tree.Trees import Trees
from antlr4 import ParseTreeWalker
from SeqDiagramsInterpreter import SequenceDiagramInterpreter
import matplotlib.pyplot as plt

def print_tree(tree, parser, indent="", is_last=True):
    if isinstance(tree, TerminalNode):
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
    sequence ComprehensiveExample {
        actor User;
        object Client;
        boundary UI;
        control Controller;
        entity Order;
        database Database;
        
        User -> UI : Select_product;
        UI => Controller : Notify_selection;
        Controller -> Database : Query_product_details;
        Database --> Controller : Return_product_data;
        Controller -> UI : Update_display;
        
        for (each_item_in_cart) {
            User -> UI : Adjust_quantity;
            UI -> Controller : Update_item_count;
            Controller -> Order : Recalculate_total;
        }
        
        alt {
            case (checkout_as_guest) {
                User -> UI : Proceed_as_guest;
                UI -> Controller : Process_guest_checkout;
            }
            case (checkout_as_member) {
                User -> UI : Login;
                UI -> Controller : Authenticate_user;
                Controller -> Database : Verify_credentials;
                Database --> Controller : Authentication_result;
                
                Controller -x> UI : Show_error_message;
            }
        }
        
        opt (apply_coupon) {
            User -> UI : Enter_coupon_code;
            UI -> Controller : Validate_coupon;
            Controller -> Database : Check_coupon_validity;
            Database --> Controller : Coupon_status;
            Controller -> Order : Apply_discount;
        }
        
        User -> Controller : Place_order;
        Controller activate;
        Controller -> Order : Create_new_order;
        Order activate;
        Order -> Database : Save_order_details;
        
        Controller <-> Order : Synchronize_order_status;
        Controller -o> Database : Request_with_timeout;
        
        Database |< Controller : Bulk_data_transfer;
        
        Order deactivate;
        Controller deactivate;
    }
    """

    input_stream = InputStream(input_string)
    lexer = SeqDiagramsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SeqDiagramsParser(stream)
    tree = parser.sequenceDiagram()

    print("=== Parse Tree ===")
    print_tree(tree, parser)

    walker = ParseTreeWalker()
    interpreter = SequenceDiagramInterpreter()

    try:
        walker.walk(interpreter, tree)
        print("\nSequence diagram generated successfully!")
        
    except Exception as e:
        print(f"\nInterpreter halted: {e}")
        import traceback
        traceback.print_exc()

    print(f"Syntax errors: {parser.getNumberOfSyntaxErrors()}")
    
    plt.show()

if __name__ == "__main__":
    main()
