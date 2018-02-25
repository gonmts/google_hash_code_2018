class cImage:

	def __init__(self):
		self.pos = (0,0) #img position on globe with lagitude and longitude
		self.time = [(0,0),(0,0)] #time frames that the image can be taken
		self.score = 0 #heuristic score of the image
