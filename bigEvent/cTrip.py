from read_file import *

class cTrip:

	def __init__(self, startPoint, endPoint, earliestStart, latestFinish):
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.earliestStart = earliestStart
		self.latestFinish = latestFinish

	def getTravelTime(self):
		return read_file.distance(self.endPoint, self.startPoint)

	def getLatestStart(self):
		return self.latestFinish - getTravelTime
