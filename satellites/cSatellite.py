from cImage import *

class cSatellite:
	def __init__(self, id, lat, longi, velocity, w, d):
		self.id = self.id
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

		self.lat = (self.lat + 324000)%(2*324000) - 324000
		self.longi = (self.longi + 648000)%(2*648000) - 648000
		self.maxCameraMov = self.maxCameraMov + self.w




	def track(self, cImage):
		self.deltax = self.lat - cImage.pos[0]
		self.deltay = self.longi - cImage.pos[1]


	def initList(self, totalFrames):
		i = 1
		originalLat = self.lat
		originalLongi = self.longi
		originalVel = self.velocity
		posList = []

		while(i <= totalFrames):
			self.updatePosition(i)
			posList += [(self.lat, self.longi)]
			i += 1

		self.lat = originalLat
		self.longi = originalLongi
		self.velocity = originalVel
		self.maxCameraMove = self.w

		return posList


	def isInRange(self, image):
		requiredX = self.lat - image.pos[0]
		requiredY = self.longi - image.pos[1]

		if(requiredX > self.limitCameraFoV or requiredX < - self.limitCameraFoV
				or requiredY > self.limitCameraFoV or requiredY < - self.limitCameraFoV): 
			return False

		deltaX = requiredX - self.deltax
		deltaY = requiredY - self.deltay

		if(deltaX > self.maxCameraMov or deltaX < - self.maxCameraMov
				or deltaY > self.maxCameraMov or deltaY < - self.maxCameraMov): 
			return False

		return True


	def isInWishfulRange(self, satpos, image):
		requiredX = satpos[0] - image.pos[0]
		requiredY = satpos[1] - image.pos[1]
		return (requiredX <= self.limitCameraFoV and requiredX >= - self.limitCameraFoV
					and requiredY <= self.limitCameraFoV and requiredY >= - self.limitCameraFoV)

