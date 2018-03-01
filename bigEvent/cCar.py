from cTrip import *
from read_file import *


class cCar:
    def __init__(self):
        self.current_pos = (0,0) #tuple
        self.onRide = False #bool
        self.destination = False #tuple
        self.completed_trips = [] #list
    
    def beginTrip(self, Trip):
        self.onRide = True
        self.destination = Trip.endPoint
        self.completed_trips += [Trip]
    
    def endTrip(self):
        self.onRide = False
        self.destination = False
    
    def timeToEndTrip(self):
        return distance(self.current_pos,self.destination)
    
    def isValid(self,Trip,t):
        res=0
        currPos=self.current_pos
        if self.onRide:
            res+= self.timeToEndTrip()
            currPos=self.destination

        res+=distance(currPos, Trip.startPoint)
        
        return res+t <= Trip.getLatestStart()
        
        
    
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
