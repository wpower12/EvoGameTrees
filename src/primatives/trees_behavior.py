import random as r
from trees_actions import *

SUCCESS, FAILURE, RUNNING = 0, 1, 2

class BTreeNode():
	def __init__(self):
		self.children = []
	def onTick():
		return RUNNING
	def __str__(self, level=0):
		ret = " "*level+self.__repr__()+"\n"
		for child in self.children:
			ret += child.__str__(level+1)
		return ret

class FallBackNode(BTreeNode):
	def onTick(self):
		for i in range(len(self.children)):
			child_status = self.children[i].onTick()
			if child_status == RUNNING:
				return RUNNING
			elif child_status == SUCCESS:
				return SUCCESS
		return FAILURE

	def __repr__(self):
		return "FallBackNode"

class SequenceNode(BTreeNode):
	def onTick(self):
		for i in range(len(self.children)):
			child_status = self.children[i].onTick()
			if child_status == RUNNING:
				return RUNNING
			elif child_status == FAILURE:
				return FAILURE
		return SUCCESS

	def __repr__(self):
		return "SequenceNode"

class NotNode(BTreeNode):
	# Return SUCCESS on FAILURE, FAILURE otherwise		
	def onTick(self):
		child_status = self.children[0].onTick()
		if child_status == FAILURE:
			return SUCCESS
		return FAILURE

	def __repr__(self):
		return "NotNode"

class LeafNode(BTreeNode):
	def __init__(self, action_tree):
		self.action_tree = action_tree

	def onTick(self):
		return self.action_tree.eval()

	def __str__(self, level):
		return " "*level+"LeafNode:"+str(self.action_tree.id)+"\n"

def get_random_internalnode():
	n = r.randint( 0, 1 )
	if n == 0:
		return FallBackNode()
	else:
		return SequenceNode()

def get_random_leafnode():
	
	return LeafNode( ActionTreeNode(r.randint(0, 100000)) )