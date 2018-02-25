class cImage:

	def __init__(self, pos, time, score):
		self.pos = pos #img position on globe with lagitude and longitude
		self.time = time #time frames that the image can be taken
		self.score = score #heuristic score of the image
