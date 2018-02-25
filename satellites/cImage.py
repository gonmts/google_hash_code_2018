class cImage:

	def __init__(self, pos, time, score):
		self.pos = pos #img position on globe with lagitude and longitude => tuple
		self.time = time #time frames that the image can be taken => list of tuples
		self.score = score #heuristic score of the image => int
		self.done = False
		self.time_done = -1
		self.sat_done = -1
