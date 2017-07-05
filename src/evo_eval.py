""" TODO
 - Instantiate the openaigym environment
 - Actually the evaluation loop
 	+ Start fresh level
 	+ on each update, parse the behavior tree to determine action
 - Connect to the module that will manage the shared stacks for use by the
   stack-based-gp actiontrees.
 - Output the full pop, with each one given their fitness score.
 - Need to define the fitness score for each environment we might encounter.
"""

class Eval():
	def __init__(self, env_type):
		self.env_type = env_type

	def eval(self, pop):
		a = 1	