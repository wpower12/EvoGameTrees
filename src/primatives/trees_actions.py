SUCCESS, FAILURE, RUNNING = 0, 1, 2

class ActionTreeNode():
	def __init__(self):
		self.children = []

	def eval(self):
		return SUCCESS