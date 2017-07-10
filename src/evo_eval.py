""" TODO
 - Instantiate the openaigym environment
 - Actually the evaluation loop
 	+ Start fresh level
 	+ on each update, parse the behavior tree to determine action
 - Connect to the module that will manage the shared stacks for use by the
   stack-based-gp actiontrees.
 - Output the full pop, with each one given their fitness score.
 - Need to define the fitness score for each environment we might encounter.
 - BIG - Implement the different evaluations for a/b trees.
 - B-trees - Normal, can keep the current one, but have to replace the species ID's with
   the relevant, best performing A-trees.
 - A-trees - Complicated - See notes on iterating over the species.
"""
import gym

class RandomAgent(object):
	def __init__(self, action_space):
		self.action_space = action_space

	def act(self, observation, reward, done):
		return self.action_space.sample()

class BTreeAgent(object):
	def __init__(self, action_space):
		self.action_space = action_space

	def act(self, observation, reward, done):
		return self.action_space.sample()

class Eval():
	def __init__(self, env_name):
		self.env = gym.make(env_name)
		self.agent = RandomAgent(self.env.action_space)

	def eval(self, pop, max_steps):
		done = False
		reward = 0
		ob = self.env.reset()
		for j in range(max_steps):
			action = self.agent.act(ob, reward, done)
			ob, reward, done, _ = self.env.step(action)
			self.env.render()
			if done: break

	def eval_btrees(self):
		a = 1

	def eval_atrees(self):
		a = 1