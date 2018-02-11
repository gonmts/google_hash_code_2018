
class VarDispatcher:

	def __init__(self, height, width):
		self.width = width
		self.height = height


	def pizza_to_cn(self, row, col, slic):
		return (slic*self.width*self.height) + row*self.width + col



	def cnf_to_max(self, var):
		slic = var // (self.width * self.height)
		col = (var - slic * (self.width * self.height)) // self.width
		row = (var - slic * (self.width * self.height)) - (col * self.width)
		return (row, col, slic)
