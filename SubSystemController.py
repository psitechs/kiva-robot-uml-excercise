#Defines Abstract SubSystem Class, Attributes and Operations

class SubSystemController:
    def __init__(self) -> None:
        pass
    #Attributes
        #denotes whether this subsystem is currently in an error state
        hasError=False

    #Operations
        #Unimplemented operation to check a subsystems error state
        def runDiagnostics():
            pass

