
class VarDispatcher:

	def __init__(self, height, width, slices):
		self.width = width
		self.height = height
		self.slices = slices
		self.aux_var_count = 0

	def pizza_to_cn(self, row, col, slic):
		return (slic*self.width*self.height) + row*self.width + col

	def cnf_to_max(self, var):
		slic = var // (self.width * self.height)
		col = (var - slic * (self.width * self.height)) // self.width
		row = (var - slic * (self.width * self.height)) - (col * self.width)
		return (row, col, slic)

	def gen_aux(self, var):
		max_var = self.width * self.height * self.slices
		res = max_var + self.aux_var_count
		self.aux_var_count += 1
		return res
