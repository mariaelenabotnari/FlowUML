# Generated from SeqDiagrams.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SeqDiagramsParser import SeqDiagramsParser
else:
    from SeqDiagramsParser import SeqDiagramsParser

# This class defines a complete listener for a parse tree produced by SeqDiagramsParser.
class SeqDiagramsListener(ParseTreeListener):

    # Enter a parse tree produced by SeqDiagramsParser#sequenceDiagram.
    def enterSequenceDiagram(self, ctx:SeqDiagramsParser.SequenceDiagramContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#sequenceDiagram.
    def exitSequenceDiagram(self, ctx:SeqDiagramsParser.SequenceDiagramContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#lifeline.
    def enterLifeline(self, ctx:SeqDiagramsParser.LifelineContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#lifeline.
    def exitLifeline(self, ctx:SeqDiagramsParser.LifelineContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#participant.
    def enterParticipant(self, ctx:SeqDiagramsParser.ParticipantContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#participant.
    def exitParticipant(self, ctx:SeqDiagramsParser.ParticipantContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#diagramName.
    def enterDiagramName(self, ctx:SeqDiagramsParser.DiagramNameContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#diagramName.
    def exitDiagramName(self, ctx:SeqDiagramsParser.DiagramNameContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#actor.
    def enterActor(self, ctx:SeqDiagramsParser.ActorContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#actor.
    def exitActor(self, ctx:SeqDiagramsParser.ActorContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#object.
    def enterObject(self, ctx:SeqDiagramsParser.ObjectContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#object.
    def exitObject(self, ctx:SeqDiagramsParser.ObjectContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#boundary.
    def enterBoundary(self, ctx:SeqDiagramsParser.BoundaryContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#boundary.
    def exitBoundary(self, ctx:SeqDiagramsParser.BoundaryContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#control.
    def enterControl(self, ctx:SeqDiagramsParser.ControlContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#control.
    def exitControl(self, ctx:SeqDiagramsParser.ControlContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#entity.
    def enterEntity(self, ctx:SeqDiagramsParser.EntityContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#entity.
    def exitEntity(self, ctx:SeqDiagramsParser.EntityContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#database.
    def enterDatabase(self, ctx:SeqDiagramsParser.DatabaseContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#database.
    def exitDatabase(self, ctx:SeqDiagramsParser.DatabaseContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#objectName.
    def enterObjectName(self, ctx:SeqDiagramsParser.ObjectNameContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#objectName.
    def exitObjectName(self, ctx:SeqDiagramsParser.ObjectNameContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#objectOnly.
    def enterObjectOnly(self, ctx:SeqDiagramsParser.ObjectOnlyContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#objectOnly.
    def exitObjectOnly(self, ctx:SeqDiagramsParser.ObjectOnlyContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#objectClass.
    def enterObjectClass(self, ctx:SeqDiagramsParser.ObjectClassContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#objectClass.
    def exitObjectClass(self, ctx:SeqDiagramsParser.ObjectClassContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#classOnly.
    def enterClassOnly(self, ctx:SeqDiagramsParser.ClassOnlyContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#classOnly.
    def exitClassOnly(self, ctx:SeqDiagramsParser.ClassOnlyContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#classPackage.
    def enterClassPackage(self, ctx:SeqDiagramsParser.ClassPackageContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#classPackage.
    def exitClassPackage(self, ctx:SeqDiagramsParser.ClassPackageContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#objectClassPackage.
    def enterObjectClassPackage(self, ctx:SeqDiagramsParser.ObjectClassPackageContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#objectClassPackage.
    def exitObjectClassPackage(self, ctx:SeqDiagramsParser.ObjectClassPackageContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#interaction.
    def enterInteraction(self, ctx:SeqDiagramsParser.InteractionContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#interaction.
    def exitInteraction(self, ctx:SeqDiagramsParser.InteractionContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#message.
    def enterMessage(self, ctx:SeqDiagramsParser.MessageContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#message.
    def exitMessage(self, ctx:SeqDiagramsParser.MessageContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#synchronous.
    def enterSynchronous(self, ctx:SeqDiagramsParser.SynchronousContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#synchronous.
    def exitSynchronous(self, ctx:SeqDiagramsParser.SynchronousContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#asynchronous.
    def enterAsynchronous(self, ctx:SeqDiagramsParser.AsynchronousContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#asynchronous.
    def exitAsynchronous(self, ctx:SeqDiagramsParser.AsynchronousContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#returnMessage.
    def enterReturnMessage(self, ctx:SeqDiagramsParser.ReturnMessageContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#returnMessage.
    def exitReturnMessage(self, ctx:SeqDiagramsParser.ReturnMessageContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#xsynchronous.
    def enterXsynchronous(self, ctx:SeqDiagramsParser.XsynchronousContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#xsynchronous.
    def exitXsynchronous(self, ctx:SeqDiagramsParser.XsynchronousContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#twoWayAsync.
    def enterTwoWayAsync(self, ctx:SeqDiagramsParser.TwoWayAsyncContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#twoWayAsync.
    def exitTwoWayAsync(self, ctx:SeqDiagramsParser.TwoWayAsyncContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#timeout.
    def enterTimeout(self, ctx:SeqDiagramsParser.TimeoutContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#timeout.
    def exitTimeout(self, ctx:SeqDiagramsParser.TimeoutContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#bulking.
    def enterBulking(self, ctx:SeqDiagramsParser.BulkingContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#bulking.
    def exitBulking(self, ctx:SeqDiagramsParser.BulkingContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#loop.
    def enterLoop(self, ctx:SeqDiagramsParser.LoopContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#loop.
    def exitLoop(self, ctx:SeqDiagramsParser.LoopContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#conditional.
    def enterConditional(self, ctx:SeqDiagramsParser.ConditionalContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#conditional.
    def exitConditional(self, ctx:SeqDiagramsParser.ConditionalContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#altCase.
    def enterAltCase(self, ctx:SeqDiagramsParser.AltCaseContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#altCase.
    def exitAltCase(self, ctx:SeqDiagramsParser.AltCaseContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#optional.
    def enterOptional(self, ctx:SeqDiagramsParser.OptionalContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#optional.
    def exitOptional(self, ctx:SeqDiagramsParser.OptionalContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#parallel.
    def enterParallel(self, ctx:SeqDiagramsParser.ParallelContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#parallel.
    def exitParallel(self, ctx:SeqDiagramsParser.ParallelContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#lifecycle.
    def enterLifecycle(self, ctx:SeqDiagramsParser.LifecycleContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#lifecycle.
    def exitLifecycle(self, ctx:SeqDiagramsParser.LifecycleContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#newObject.
    def enterNewObject(self, ctx:SeqDiagramsParser.NewObjectContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#newObject.
    def exitNewObject(self, ctx:SeqDiagramsParser.NewObjectContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#deleteObject.
    def enterDeleteObject(self, ctx:SeqDiagramsParser.DeleteObjectContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#deleteObject.
    def exitDeleteObject(self, ctx:SeqDiagramsParser.DeleteObjectContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#activation.
    def enterActivation(self, ctx:SeqDiagramsParser.ActivationContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#activation.
    def exitActivation(self, ctx:SeqDiagramsParser.ActivationContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#deactivation.
    def enterDeactivation(self, ctx:SeqDiagramsParser.DeactivationContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#deactivation.
    def exitDeactivation(self, ctx:SeqDiagramsParser.DeactivationContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#note.
    def enterNote(self, ctx:SeqDiagramsParser.NoteContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#note.
    def exitNote(self, ctx:SeqDiagramsParser.NoteContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#stereotype.
    def enterStereotype(self, ctx:SeqDiagramsParser.StereotypeContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#stereotype.
    def exitStereotype(self, ctx:SeqDiagramsParser.StereotypeContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#synchronousStereo.
    def enterSynchronousStereo(self, ctx:SeqDiagramsParser.SynchronousStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#synchronousStereo.
    def exitSynchronousStereo(self, ctx:SeqDiagramsParser.SynchronousStereoContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#returnStereo.
    def enterReturnStereo(self, ctx:SeqDiagramsParser.ReturnStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#returnStereo.
    def exitReturnStereo(self, ctx:SeqDiagramsParser.ReturnStereoContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#xsynchronousStereo.
    def enterXsynchronousStereo(self, ctx:SeqDiagramsParser.XsynchronousStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#xsynchronousStereo.
    def exitXsynchronousStereo(self, ctx:SeqDiagramsParser.XsynchronousStereoContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#twoWayAsyncStereo.
    def enterTwoWayAsyncStereo(self, ctx:SeqDiagramsParser.TwoWayAsyncStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#twoWayAsyncStereo.
    def exitTwoWayAsyncStereo(self, ctx:SeqDiagramsParser.TwoWayAsyncStereoContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#timeoutStereo.
    def enterTimeoutStereo(self, ctx:SeqDiagramsParser.TimeoutStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#timeoutStereo.
    def exitTimeoutStereo(self, ctx:SeqDiagramsParser.TimeoutStereoContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#bulkingStereo.
    def enterBulkingStereo(self, ctx:SeqDiagramsParser.BulkingStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#bulkingStereo.
    def exitBulkingStereo(self, ctx:SeqDiagramsParser.BulkingStereoContext):
        pass


    # Enter a parse tree produced by SeqDiagramsParser#asynchronousStereo.
    def enterAsynchronousStereo(self, ctx:SeqDiagramsParser.AsynchronousStereoContext):
        pass

    # Exit a parse tree produced by SeqDiagramsParser#asynchronousStereo.
    def exitAsynchronousStereo(self, ctx:SeqDiagramsParser.AsynchronousStereoContext):
        pass



del SeqDiagramsParser