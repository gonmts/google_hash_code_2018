from cTrip import *

class cCar:
	def __init__(self, id):
		self.current_pos = (0,0) #tuple
		self.onRide = False #bool
		self.destination = False #tuple
		self.completed_trips = [] #list

	def beginTrip(self, cTrip):
		onRide = True
		self.destination = cTrip.endPoint
		self.completed_trips += [cTrip]


	def endTrip(self):
		onRide = False
		self.destination = False
