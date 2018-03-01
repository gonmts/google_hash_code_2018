from read_file import *

class cTrip:

	def __init__(self, id, startPoint, endPoint, earliestStart, latestFinish):
		self.id = id
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish

	def getTravelTime(self):
		return 0 #distance(self.endPoint, self.startPoint)

	def getLatestStart(self):
		return self.latestFinish - self.getTravelTime()
