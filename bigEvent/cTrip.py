def distance(start, finish):
    startX, startY = start
    finishX, finishY = finish
    return abs(finishX - startX) + abs(finishY - startY)

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
