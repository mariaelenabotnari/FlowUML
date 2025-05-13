from SeqDiagramsListener import SeqDiagramsListener
from SeqDiagramsParser import SeqDiagramsParser
from SequenceDiagramVisualizer import SequenceDiagramVisualizer

class SequenceDiagramInterpreter(SeqDiagramsListener):
    def __init__(self):
        self.defined_lifelines = set()
        self.semantic_errors = []
        self.visualizer = SequenceDiagramVisualizer()
        self.current_nesting_level = 0
        self.active_lifelines = set()

    def _strip(self, token):
        if token and token.getText().startswith('"'):
            return token.getText().strip('"')
        return token.getText() if token else ""

    def _check_lifeline(self, name, ctx):
        if name not in self.defined_lifelines:
            self.semantic_errors.append(f"Semantic Error: Lifeline '{name}' used before declaration at line {ctx.start.line}.")

    def enterSequenceDiagram(self, ctx):
        if ctx.IDENTIFIER():
            name = self._strip(ctx.IDENTIFIER())
            print(f"[DEBUG] SequenceDiagram: {name}")
            if name:
                self.visualizer.set_title(name)
        else:
            print(f"[DEBUG] SequenceDiagram without a name")

    def enterActor(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Actor: {name}")
        self.defined_lifelines.add(name)
        self.visualizer.add_participant(name, "actor")

    def enterObject(self, ctx):
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

    def enterSynchronous(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Synchronous Message: {src} -> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        
        msg_type = "->"
        if ctx.synchronousStereo():
            stereotype = self._strip(ctx.synchronousStereo().STEREOTYPE())
            print(f"[DEBUG] Stereotype: {stereotype}")
            if "create" in stereotype:
                msg_type = "->>"
                
        self.visualizer.add_message(src, dst, display_msg, msg_type)
    
    def enterAsynchronous(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Asynchronous Message: {src} => {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-->")
        
    def enterReturnMessage(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Return Message: {src} --> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-->")
    
    def enterXsynchronous(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Destruction Message: {src} -x> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-x>")
    
    def enterTwoWayAsync(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Two-way Async: {src} <-> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "<->")
    
    def enterTimeout(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Timeout Message: {src} -o> {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "-o>")
        
    def enterBulking(self, ctx):
        src = self._strip(ctx.IDENTIFIER(0))
        dst = self._strip(ctx.IDENTIFIER(1))
        msg = self._strip(ctx.IDENTIFIER(2))
        
        display_msg = msg.replace('_', ' ')
        
        print(f"[DEBUG] Bulking Message: {src} |< {dst}: {display_msg}")
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        self.visualizer.add_message(src, dst, display_msg, "|<")
    
    def enterLoop(self, ctx):
        condition = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Loop: {condition}")
        self.current_nesting_level += 1
        
    def exitLoop(self, ctx):
        self.current_nesting_level -= 1
        print(f"[DEBUG] End Loop")
    
    def enterConditional(self, ctx):
        print(f"[DEBUG] Alt")
        self.current_nesting_level += 1
        
    def exitConditional(self, ctx):
        self.current_nesting_level -= 1
        print(f"[DEBUG] End Alt")
    
    def enterAltCase(self, ctx):
        condition = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Case: {condition}")
    
    def enterOptional(self, ctx):
        condition = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Opt: {condition}")
        self.current_nesting_level += 1
        
    def exitOptional(self, ctx):
        self.current_nesting_level -= 1
        print(f"[DEBUG] End Opt")
        
    def enterParallel(self, ctx):
        print(f"[DEBUG] Par")
        self.current_nesting_level += 1
        
    def exitParallel(self, ctx):
        self.current_nesting_level -= 1
        print(f"[DEBUG] End Par")
        
    def enterActivation(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Activate: {name}")
        self._check_lifeline(name, ctx)
        self.active_lifelines.add(name)
        self.visualizer.add_activation(name)
        
    def enterDeactivation(self, ctx):
        name = self._strip(ctx.IDENTIFIER())
        print(f"[DEBUG] Deactivate: {name}")
        self._check_lifeline(name, ctx)
        if name not in self.active_lifelines:
            self.semantic_errors.append(f"Semantic Error: Tried to deactivate inactive lifeline '{name}' at line {ctx.start.line}.")
        else:
            self.active_lifelines.remove(name)
        self.visualizer.add_deactivation(name)
        
    def exitSequenceDiagram(self, ctx):
        for lifeline in list(self.active_lifelines):
            self.visualizer.add_deactivation(lifeline)
            print(f"[DEBUG] Auto-deactivate: {lifeline}")
        self.active_lifelines.clear()
