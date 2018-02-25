class cSatellite:
	def __init__(self, lat, longi, velocity, w, d):
		self.lat = lat
		self.longi = longi
		self.maxCameraMov = w
		self.w = w
		self.limitCameraFoV = d
		self.velocity = velocity
		self.deltax = 0
		self.deltay = 0


	def updatePosition(self, t):
		if( self.lat + self.velocity >= -324000 and self.lat + self.velocity <= 324000):
			self.lat = self.lat + self.velocity
			self.longi = self.longi - 15
			self.velocity = self.originalVelocity
		elif( self.lat + self.velocity > 324000 ):
			self.lat = 648000 - (self.lat + self.velocity)
			self.longi = -648000 + (self.longi - 15)
			self.velocity = - self.velocity
		elif( self.lat + self.velocity < -324000 ):
			self.lat = - 648000 - (self.lat + self.velocity)
			self.longi = -648000 + (self.longi - 15)
			self.velocity = - self.velocity
		else:
			print('Ooops! This should never happen! :s')

		self.maxCameraMove = self.maxCameraMove + self.w



	def isInRange(self, image, t):
		requiredX = self.lat - image.pos[0]
		requiredY = self.longi - image.pos[1]

		if(requiredX > self.maxCameraMove or requiredX < - self.maxCameraMove
				or requiredY > self.maxCameraMove or requiredY < - self.maxCameraMove): 
			return False






