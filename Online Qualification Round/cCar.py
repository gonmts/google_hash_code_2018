from cTrip import *
from read_file import *


class cCar:
    def __init__(self):
        self.current_pos = (0,0) #tuple
        self.onRide = False #bool
        self.destination = False #tuple
        self.completed_trips = [] #list
        self.lastUpdate = -1
        self.remainingDistance = -1

    def beginTrip(self, Trip, t):
        self.onRide = True
        self.destination = Trip.endPoint
        self.completed_trips += [Trip]
        self.lastUpdate = t;
        self.remainingDistance = distance(self.current_pos, self.destination)

    def endTrip(self):
        self.onRide = False
        self.destination = False
        self.current_pos = self.destination
        self.remainingDistance = 0

    def update(self, t):
    	self.remainingDistance -= t - self.lastUpdate
    	self.lastUpdate = t
    	if self.remainingDistance == 0:
    		self.endTrip()



    def timeToEndTrip(self):
        return distance(self.current_pos, self.destination)

    def isValid(self,Trip,t):
        res=0
        #currPos=self.current_pos
        if self.onRide:
            res+= self.timeToEndTrip()
            #currPos=self.destination

        self.update(t)
        res+= self.remainingDistance  #distance(currPos, Trip.startPoint)

        return res+t <= Trip.getLatestStart()



    def score(self,Trip,t):
        res=0
        #currPos=self.current_pos
        if self.onRide:
            res+= self.timeToEndTrip()
            #currPos=self.destination

        res += self.remainingDistance

        if ( res+ t)< Trip.earliestStart:
            res-=Trip.bonus

        return res
