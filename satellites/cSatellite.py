class Satellite:
	def __init__(self):
		pass


	def main(self, lat, longi, velocity, limitx, limity):
		self.lat = lat
		self.longi = longi
		self.limitx = limitx
		self.limity = limity
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


