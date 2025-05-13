# Generated from SeqDiagrams.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SeqDiagramsParser import SeqDiagramsParser
else:
    from SeqDiagramsParser import SeqDiagramsParser

# This class defines a complete generic visitor for a parse tree produced by SeqDiagramsParser.

class SeqDiagramsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SeqDiagramsParser#sequenceDiagram.
    def visitSequenceDiagram(self, ctx:SeqDiagramsParser.SequenceDiagramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#lifeline.
    def visitLifeline(self, ctx:SeqDiagramsParser.LifelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#participant.
    def visitParticipant(self, ctx:SeqDiagramsParser.ParticipantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#diagramName.
    def visitDiagramName(self, ctx:SeqDiagramsParser.DiagramNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#actor.
    def visitActor(self, ctx:SeqDiagramsParser.ActorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#object.
    def visitObject(self, ctx:SeqDiagramsParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#boundary.
    def visitBoundary(self, ctx:SeqDiagramsParser.BoundaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#control.
    def visitControl(self, ctx:SeqDiagramsParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#entity.
    def visitEntity(self, ctx:SeqDiagramsParser.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#database.
    def visitDatabase(self, ctx:SeqDiagramsParser.DatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#objectName.
    def visitObjectName(self, ctx:SeqDiagramsParser.ObjectNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#objectOnly.
    def visitObjectOnly(self, ctx:SeqDiagramsParser.ObjectOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#objectClass.
    def visitObjectClass(self, ctx:SeqDiagramsParser.ObjectClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#classOnly.
    def visitClassOnly(self, ctx:SeqDiagramsParser.ClassOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#classPackage.
    def visitClassPackage(self, ctx:SeqDiagramsParser.ClassPackageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#objectClassPackage.
    def visitObjectClassPackage(self, ctx:SeqDiagramsParser.ObjectClassPackageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#interaction.
    def visitInteraction(self, ctx:SeqDiagramsParser.InteractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#message.
    def visitMessage(self, ctx:SeqDiagramsParser.MessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#synchronous.
    def visitSynchronous(self, ctx:SeqDiagramsParser.SynchronousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#asynchronous.
    def visitAsynchronous(self, ctx:SeqDiagramsParser.AsynchronousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#returnMessage.
    def visitReturnMessage(self, ctx:SeqDiagramsParser.ReturnMessageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#xsynchronous.
    def visitXsynchronous(self, ctx:SeqDiagramsParser.XsynchronousContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#twoWayAsync.
    def visitTwoWayAsync(self, ctx:SeqDiagramsParser.TwoWayAsyncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#timeout.
    def visitTimeout(self, ctx:SeqDiagramsParser.TimeoutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#bulking.
    def visitBulking(self, ctx:SeqDiagramsParser.BulkingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#loop.
    def visitLoop(self, ctx:SeqDiagramsParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#conditional.
    def visitConditional(self, ctx:SeqDiagramsParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#altCase.
    def visitAltCase(self, ctx:SeqDiagramsParser.AltCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#optional.
    def visitOptional(self, ctx:SeqDiagramsParser.OptionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#parallel.
    def visitParallel(self, ctx:SeqDiagramsParser.ParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#lifecycle.
    def visitLifecycle(self, ctx:SeqDiagramsParser.LifecycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#newObject.
    def visitNewObject(self, ctx:SeqDiagramsParser.NewObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#deleteObject.
    def visitDeleteObject(self, ctx:SeqDiagramsParser.DeleteObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#activation.
    def visitActivation(self, ctx:SeqDiagramsParser.ActivationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#deactivation.
    def visitDeactivation(self, ctx:SeqDiagramsParser.DeactivationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#note.
    def visitNote(self, ctx:SeqDiagramsParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#stereotype.
    def visitStereotype(self, ctx:SeqDiagramsParser.StereotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#synchronousStereo.
    def visitSynchronousStereo(self, ctx:SeqDiagramsParser.SynchronousStereoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#returnStereo.
    def visitReturnStereo(self, ctx:SeqDiagramsParser.ReturnStereoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#xsynchronousStereo.
    def visitXsynchronousStereo(self, ctx:SeqDiagramsParser.XsynchronousStereoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#twoWayAsyncStereo.
    def visitTwoWayAsyncStereo(self, ctx:SeqDiagramsParser.TwoWayAsyncStereoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#timeoutStereo.
    def visitTimeoutStereo(self, ctx:SeqDiagramsParser.TimeoutStereoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#bulkingStereo.
    def visitBulkingStereo(self, ctx:SeqDiagramsParser.BulkingStereoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeqDiagramsParser#asynchronousStereo.
    def visitAsynchronousStereo(self, ctx:SeqDiagramsParser.AsynchronousStereoContext):
        return self.visitChildren(ctx)



del SeqDiagramsParser