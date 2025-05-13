from SeqDiagramsListener import SeqDiagramsListener
from SeqDiagramsParser import SeqDiagramsParser
from SequenceDiagramVisualizer import SequenceDiagramVisualizer

class SequenceDiagramInterpreter(SeqDiagramsListener):
    def __init__(self):
        self.defined_lifelines = set()
        self.semantic_errors = []
        self.visualizer = SequenceDiagramVisualizer()
        self.current_nesting_level = 0
        self.active_lifelines = set()  # Track activated lifelines

    def _strip(self, token):
        if token and token.getText().startswith('"'):
            return token.getText().strip('"')
        return token.getText() if token else ""

    def _check_lifeline(self, name, ctx):
        if name not in self.defined_lifelines:
            self.semantic_errors.append(f"Semantic Error: Lifeline '{name}' used before declaration at line {ctx.start.line}.")

    # Sequence diagram
    def enterSequenceDiagram(self, ctx):
        if ctx.IDENTIFIER():
            name = self._strip(ctx.IDENTIFIER())
            print(f"[DEBUG] SequenceDiagram: {name}")
            if name:
                self.visualizer.set_title(name)
        # Handle case where there is no title
        else:
            print(f"[DEBUG] SequenceDiagram without a name")

    # Participant declarations
    def enterActor(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Actor: {name}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "actor")

    def enterObject(self, ctx):
        # Handle different object name formats
        object_name_ctx = ctx.objectName()
        if object_name_ctx.objectOnly():
            name = self._strip(object_name_ctx.objectOnly().IDENTIFIER())
            class_type = "Object"
        elif object_name_ctx.objectClass():
            name = self._strip(object_name_ctx.objectClass().IDENTIFIER(0))
            class_type = self._strip(object_name_ctx.objectClass().IDENTIFIER(1))
        elif object_name_ctx.classOnly():
            name = "AnonymousObject"
            class_type = self._strip(object_name_ctx.classOnly().IDENTIFIER())
        elif object_name_ctx.classPackage():
            name = "AnonymousObject"
            pkg = self._strip(object_name_ctx.classPackage().IDENTIFIER(0))
            cls = self._strip(object_name_ctx.classPackage().IDENTIFIER(1))
            class_type = f"{pkg}::{cls}"
        elif object_name_ctx.objectClassPackage():
            name = self._strip(object_name_ctx.objectClassPackage().IDENTIFIER(0))
            pkg = self._strip(object_name_ctx.objectClassPackage().IDENTIFIER(1))
            cls = self._strip(object_name_ctx.objectClassPackage().IDENTIFIER(2))
            class_type = f"{pkg}::{cls}"
        else:
            name = "UnknownObject"
            class_type = "Unknown"
            
        print(f"[DEBUG] Object: {name}, class: {class_type}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "object")
    
    def enterBoundary(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Boundary: {name}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "boundary")
        
    def enterControl(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Control: {name}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "control")
        
    def enterEntity(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Entity: {name}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "entity")
        
    def enterDatabase(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Database: {name}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "database")

    # Message handling
    def enterSynchronous(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Synchronous Message: {src} -> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        
        # Check if the message has a stereotype
        msg_type = "->"
        if ctx.synchronousStereo():
            stereotype = self._strip(ctx.synchronousStereo().STEREOTYPE())
            print(f"[DEBUG] Stereotype: {stereotype}")
            if "create" in stereotype:
                # Creation message
                msg_type = "->>"
                
        self.visualizer.add_message(src, dst, display_msg, msg_type)
    
    def enterAsynchronous(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Asynchronous Message: {src} => {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-->")
        
    def enterReturnMessage(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Return Message: {src} --> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-->")
    
    def enterXsynchronous(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Destruction Message: {src} -x> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-x>")
    
    def enterTwoWayAsync(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Two-way Async: {src} <-> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "<->")
    
    def enterTimeout(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Timeout Message: {src} -o> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-o>")
        
    def enterBulking(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        # Transform underscores to spaces for display
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Bulking Message: {src} |< {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "|<")
    
    # Control structures
    def enterLoop(self, ctx):
        condition = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Loop: {condition}")
        self.current_nesting_level += 1
        # Use the new control block visualization
        self.visualizer.start_loop(condition)
    
    def exitLoop(self, ctx):
        self.current_nesting_level -= 1
        self.visualizer.end_loop()
    
    def enterConditional(self, ctx):
        print(f"[DEBUG] Alt: conditional block")
        self.current_nesting_level += 1
        # Use the new control block visualization
        self.visualizer.start_alt()
    
    def exitConditional(self, ctx):
        self.current_nesting_level -= 1
        self.visualizer.end_alt()
    
    def enterAltCase(self, ctx):
        condition = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Case: {condition}")
        # Use the new branch method
        self.visualizer.add_alt_branch(condition)
    
    def enterOptional(self, ctx):
        condition = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Optional: {condition}")
        self.current_nesting_level += 1
        # Use the new control block visualization
        self.visualizer.start_opt(condition)
    
    def exitOptional(self, ctx):
        self.current_nesting_level -= 1
        self.visualizer.end_opt()
    
    def enterParallel(self, ctx):
        print(f"[DEBUG] Parallel block")
        self.current_nesting_level += 1
        self.visualizer.add_note("Par: parallel execution")
    
    def exitParallel(self, ctx):
        self.current_nesting_level -= 1
    
    # Activation/Deactivation
    def enterActivation(self, ctx):
        lifeline = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Activation: {lifeline}")
        self._check_lifeline(lifeline, ctx)
        self.active_lifelines.add(lifeline)
        self.visualizer.add_activation(lifeline)
    
    def enterDeactivation(self, ctx):
        lifeline = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Deactivation: {lifeline}")
        self._check_lifeline(lifeline, ctx)
        if lifeline in self.active_lifelines:
            self.active_lifelines.remove(lifeline)
            self.visualizer.end_activation(lifeline)
    
    # Finish processing
    def exitSequenceDiagram(self, ctx):
        # Auto-end any remaining activations
        for lifeline in list(self.active_lifelines):
            self.visualizer.end_activation(lifeline)
            
        if self.semantic_errors:
            print("\nErrors:")
            for err in self.semantic_errors:
                print(err)
            raise Exception("Semantic validation failed.")
        self.visualizer.save("sequence_diagram.png")
