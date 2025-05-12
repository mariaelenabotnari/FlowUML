from SeqDiagramsListener import SeqDiagramsListener
from SeqDiagramsParser import SeqDiagramsParser

class SequenceDiagramInterpreter(SeqDiagramsListener):
    def enterSequenceDiagram(self, ctx: SeqDiagramsParser.SequenceDiagramContext):
        name = ctx.STRING().getText().strip('"')
        print(f"\n>>> Sequence Diagram: {name}")

    def enterActor(self, ctx: SeqDiagramsParser.ActorContext):
        print(f"Actor: {ctx.STRING().getText().strip('"')}")

    def enterObject(self, ctx: SeqDiagramsParser.ObjectContext):
        obj_name = ctx.objectName().getText().replace(':', ': ')
        print(f"Object: {obj_name}")

    def enterBoundary(self, ctx: SeqDiagramsParser.BoundaryContext):
        print(f"Boundary: {ctx.STRING().getText().strip('"')}")

    def enterControl(self, ctx: SeqDiagramsParser.ControlContext):
        print(f"Control: {ctx.STRING().getText().strip('"')}")

    def enterEntity(self, ctx: SeqDiagramsParser.EntityContext):
        print(f"Entity: {ctx.STRING().getText().strip('"')}")

    def enterDatabase(self, ctx: SeqDiagramsParser.DatabaseContext):
        print(f"Database: {ctx.STRING().getText().strip('"')}")

    def enterSynchronous(self, ctx: SeqDiagramsParser.SynchronousContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} -> {dst} : {msg}")

    def enterAsynchronous(self, ctx: SeqDiagramsParser.AsynchronousContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} => {dst} : {msg}")

    def enterReturnMessage(self, ctx: SeqDiagramsParser.ReturnMessageContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} <-- {dst} : {msg}")

    def enterXsynchronous(self, ctx: SeqDiagramsParser.XsynchronousContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} -x> {dst} : {msg}")

    def enterTwoWayAsync(self, ctx: SeqDiagramsParser.TwoWayAsyncContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} <-> {dst} : {msg}")

    def enterTimeout(self, ctx: SeqDiagramsParser.TimeoutContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} -o> {dst} : {msg}")

    def enterBulking(self, ctx: SeqDiagramsParser.BulkingContext):
        src = ctx.STRING(0).getText().strip('"')
        dst = ctx.STRING(1).getText().strip('"')
        msg = ctx.STRING(2).getText().strip('"')
        print(f"{src} |< {dst} : {msg}")

    def enterActivation(self, ctx: SeqDiagramsParser.ActivationContext):
        participant = ctx.STRING().getText().strip('"')
        print(f"activate {participant}")

    def enterDeactivation(self, ctx: SeqDiagramsParser.DeactivationContext):
        participant = ctx.STRING().getText().strip('"')
        print(f"deactivate {participant}")

    def enterNote(self, ctx: SeqDiagramsParser.NoteContext):
        note = ctx.STRING().getText().strip('"')
        print(f"note: {note}")

    def enterNewObject(self, ctx: SeqDiagramsParser.NewObjectContext):
        obj = ctx.STRING().getText().strip('"')
        print(f"new {obj}")

    def enterDeleteObject(self, ctx: SeqDiagramsParser.DeleteObjectContext):
        obj = ctx.STRING().getText().strip('"')
        print(f"delete {obj}")
