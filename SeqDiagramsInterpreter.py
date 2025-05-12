from SeqDiagramsListener import SeqDiagramsListener
from SeqDiagramsParser import SeqDiagramsParser

class SequenceDiagramInterpreter(SeqDiagramsListener):
    def __init__(self):
        self.defined_lifelines = set()
        self.semantic_errors = []

    def _strip(self, token):
        return token.getText().strip('"') if token else ""

    def _check_lifeline(self, name, ctx):
        if name not in self.defined_lifelines:
            self.semantic_errors.append(f"Semantic Error: Lifeline '{name}' used before declaration at line {ctx.start.line}.")

    def enterSequenceDiagram(self, ctx: SeqDiagramsParser.SequenceDiagramContext):
        name = self._strip(ctx.STRING())
        print(f"\n>>> Sequence Diagram: {name}")

    def enterActor(self, ctx: SeqDiagramsParser.ActorContext):
        name = self._strip(ctx.STRING())
        print(f"Actor: {name}")
        self.defined_lifelines.add(name)

    def enterObject(self, ctx: SeqDiagramsParser.ObjectContext):
        obj_name = ctx.objectName().getText().replace(':', ': ')
        print(f"Object: {obj_name}")
        if hasattr(ctx.objectName(), "objectOnly"):
            lifeline = self._strip(ctx.objectName().objectOnly().STRING())
        elif hasattr(ctx.objectName(), "objectClass"):
            lifeline = self._strip(ctx.objectName().objectClass().STRING(0))
        else:
            lifeline = self._strip(ctx.objectName().getText().split(':')[0])
        self.defined_lifelines.add(lifeline)

    def enterBoundary(self, ctx: SeqDiagramsParser.BoundaryContext):
        name = self._strip(ctx.STRING())
        print(f"Boundary: {name}")
        self.defined_lifelines.add(name)

    def enterControl(self, ctx: SeqDiagramsParser.ControlContext):
        name = self._strip(ctx.STRING())
        print(f"Control: {name}")
        self.defined_lifelines.add(name)

    def enterEntity(self, ctx: SeqDiagramsParser.EntityContext):
        name = self._strip(ctx.STRING())
        print(f"Entity: {name}")
        self.defined_lifelines.add(name)

    def enterDatabase(self, ctx: SeqDiagramsParser.DatabaseContext):
        name = self._strip(ctx.STRING())
        print(f"Database: {name}")
        self.defined_lifelines.add(name)

    def enterSynchronous(self, ctx: SeqDiagramsParser.SynchronousContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} -> {dst} : {msg}")

    def enterAsynchronous(self, ctx: SeqDiagramsParser.AsynchronousContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} => {dst} : {msg}")

    def enterReturnMessage(self, ctx: SeqDiagramsParser.ReturnMessageContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} <-- {dst} : {msg}")

    def enterXsynchronous(self, ctx: SeqDiagramsParser.XsynchronousContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} -x> {dst} : {msg}")

    def enterTwoWayAsync(self, ctx: SeqDiagramsParser.TwoWayAsyncContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} <-> {dst} : {msg}")

    def enterTimeout(self, ctx: SeqDiagramsParser.TimeoutContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} -o> {dst} : {msg}")

    def enterBulking(self, ctx: SeqDiagramsParser.BulkingContext):
        src = self._strip(ctx.STRING(0))
        dst = self._strip(ctx.STRING(1))
        msg = self._strip(ctx.STRING(2))
        self._check_lifeline(src, ctx)
        self._check_lifeline(dst, ctx)
        print(f"{src} |< {dst} : {msg}")

    def enterActivation(self, ctx: SeqDiagramsParser.ActivationContext):
        participant = self._strip(ctx.STRING())
        self._check_lifeline(participant, ctx)
        print(f"activate {participant}")

    def enterDeactivation(self, ctx: SeqDiagramsParser.DeactivationContext):
        participant = self._strip(ctx.STRING())
        self._check_lifeline(participant, ctx)
        print(f"deactivate {participant}")

    def enterNote(self, ctx: SeqDiagramsParser.NoteContext):
        note = self._strip(ctx.STRING())
        print(f"note: {note}")

    def enterNewObject(self, ctx: SeqDiagramsParser.NewObjectContext):
        obj = self._strip(ctx.STRING())
        self.defined_lifelines.add(obj)
        print(f"new {obj}")

    def enterDeleteObject(self, ctx: SeqDiagramsParser.DeleteObjectContext):
        obj = self._strip(ctx.STRING())
        self._check_lifeline(obj, ctx)
        print(f"delete {obj}")

    def exitSequenceDiagram(self, ctx: SeqDiagramsParser.SequenceDiagramContext):
        if self.semantic_errors:
            print("\nErrors:")
            for err in self.semantic_errors:
                print(err)
            raise Exception("Semantic validation failed.")
