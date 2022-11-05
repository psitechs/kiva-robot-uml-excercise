import SubSystemController
import Battery
import Navigation

batteryXYZ = Battery.BatteryController(4)

#Navigating to a charger and beginning a charge cycle
batteryXYZ.navigateToCharger()
batteryXYZ.startChargeCycle()

#Navigation Cycle
#Instantiating Objects
navSys = Navigation.NavigationController(254,653)
cam1 = Navigation.Camera(1080,"down")
cam2 = Navigation.Camera(1080,"up")
rateG = Navigation.RateGyro(75)
accel1 = Navigation.Accelerometer(3,50)
encoder1 = Navigation.Encoder("Digital","Optical")

#Nav System calls for location data
navSys.callForLocationData()

