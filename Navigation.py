#imports required packages
from SubSystemController import SubSystemController

#Defines Navigation Classes, Attributes and Operations

class NavigationController(SubSystemController):
        def __init__(self, currentLocation, destination) -> None:
         super().__init__()
        #Attributes
        #denotes the number of modules this controller can manage at once
         self.currentLocation = currentLocation
         self.destination = destination
        
    #Operations
        #uses current location data and an external barcode mapping database to chart a course to the destination 
        def locateDestination(self):
            print("Charting a course to the destination!")
        #makes calls to navigate package methods to intake various navigation data
        def callForLocationData(self):
            print("Requesting navigation data!")


class Camera():
        def __init__(self, resolution, orientation) -> None:
        #Attributes
        #denotes the number of modules this controller can manage at once
         self.resolution = resolution
         self.orientation = orientation
        
    #Operations
        #takes a picture of the floor barcode or product rack barcode depending on orientation
        def scanBarcode(self):
            print("Scanning barcode either on the floor or on a product rack!")
        #sends current location info to navigation system based off the last scanned floor barcode
        def sendCurrentLocation(self):
            print("Sending current coordinated based of scanned floor barcode")
        #sends the navigation system info on the current product rack held
        def sendCurrentPayload(self):
            print("Send info on the current payload!")

class Accelerometer():
        def __init__(self, currentAccelRate, range) -> None:
        #Attributes
        #denotes the current rate of acceleration for this drive unit
         self.currentAccelRate = currentAccelRate
        #denotes the max and min speed this accelerometer can detect accurately
         self.range = range
        
    #Operations
        #detects how fast the drive unit is currently accelerating
        def detectAccelRate(self):
            print("Assessing acceleration!")

class RateGyro():
        def __init__(self, maxMeasurableRotationRate) -> None:
        #Attributes
        #denotes maximum rotation speed this gyro can detect
         self.maxMeasurableRotationRate = maxMeasurableRotationRate
        
    #Operations
        #measures the angular velocity of the drive unit
        def measureAngularVelocity(self):
            print("Measuring drive unit angular velocity!")

class Encoder():
        def __init__(self, signalType, encoderType) -> None:
        #Attributes
        #denotes the type of signal this encoder can receive, usually digital or analog
         self.signalType = signalType
        #denotes the type of encoder, Mechanical, Optical, Magnetic, or Electromagnetic induction
         self.encoderType = encoderType
        
    #Operations
        #calls on the encoder to discern the angle that a wheel is facing
        def detectWheelOrientation(self):
            print("Measuring the angle orientation of a wheel!")