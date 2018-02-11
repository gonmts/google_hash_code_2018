
class VarDispatcher:

	def __init__(self, width, height):
		self.width = width
		self.height = height


	def pizza_to_cn(self, row, col, slic):
		#return row + self.height*(col + self.width*slic)
		return (row*self.width + col)*self.heigh + slic
		#return slic*self.width*self.height + col*self.width + row



	def cnf_to_max(self, var):
		row = var % self.height
		col = (var - row)/self.height % self.width
		slic = ((var - row)/self.height - col) / self.width
		#row = var % self.width
		#col = (var - row)/self.widht  % self.height
		#slic = ((var - row)/self.width - col) / self.height
		return (row, col, slic)