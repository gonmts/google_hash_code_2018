from cTrip import *
from read_file import *

class cCar:
	def __init__(self):
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

        
    def timeToEndTrip(self):
        return distance(self.current_pos,self.destination)
        
    def score(self,Trip,t):
        res=0
        currPos=self.current_pos
        if self.onRide:
            res+= self.timeToEndTrip()
            currPos=self.destination
        
        res+=distance(currPos, Trip.startPoint)
        
        if ( res+ t)< Trip.earliestStart:
            res-=Trip.bonus
            
        return res
