from read_file import *

class cTrip:

	def __init__(self, id, startPoint, endPoint, earliestStart, latestFinish, bonus):
		self.id = id
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish
		self.bonus = bonus

	def getTravelTime(self):
		return distance(self.startPoint, self.endPoint)

	def getLatestStart(self):
		return self.latestFinish - self.getTravelTime()
