from cTrip import *

class cCar:
	def __init__(self):
		self.current_pos = (0,0) #tuple
		self.onRide = False #bool
		self.destination = False #tuple 

	def beginTrip(self, cTrip):
		onRide = True
		self.destination = cTrip.endPoint


	def endTrip(self):
		onRide = False
		self.destination = False