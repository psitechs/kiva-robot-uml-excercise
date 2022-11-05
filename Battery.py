#imports required packages
from SubSystemController import SubSystemController

#Defines Battery Classes, Attributes and Operations

class BatteryController(SubSystemController):
        def __init__(self, moduleCapacity) -> None:
         super().__init__()
         self.moduleCapacity = moduleCapacity
    #Attributes
        #denotes the number of modules this controller can manage at once
        
    #Operations
        #calls on the navigation subsystem to chart a course for the nearest charger
        def navigateToCharger(self):
            print("Requesting Navigation System guide unit to charger!")
        #controls the minimum level a cell can get to before it will no longer be drawn from
        def setDischargelevel(self):
            print("Setting the minimum discharge level for cells")
        #directs modules to start a charge cycle
        def startChargeCycle(self):
            print("Starting charge!")
        #directs modules to start a charge cycle
        def stopChargeCycle(self):
            print("Stopping charge!")
class BatteryModule():
    #Attributes
        #denotes the rate at which this module can discharge energy
        dischargeRate = 10

    #Operations
        #allows current to pass to cells
        def charge():
            print("Sending energy to battery cells!")
        #allows current to pass to motors
        def discharge():
            print("Sending energy to motors!")

class BatteryCell():
    #Attributes
        #denotes the energy density of this cell
        energyDensity:int
        #denotes the max energy this cell can hold
        maxEnergyCapacity:int
        #denotes the time to completely charge this cell in seconds
        chargeCycleTime:type
    #Operations
        #allows current to pass into of the cell
        def charge():
            print("Storing energy!")
        #allows current to pass out of the cell
        def discharge():
            print("Releasing energy!")
