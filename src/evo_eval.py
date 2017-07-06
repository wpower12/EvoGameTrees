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
import gym

MAX_STEPS = 200

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
	def __init__(self, env_type):
		self.env_type = env_type
		self.env = gym.make('SpaceInvaders-v0')
		self.agent = RandomAgent(self.env.action_space)

	def eval(self, pop):
		done = False
		reward = 0
		ob = self.env.reset()
		for j in range(MAX_STEPS):
			action = self.agent.act(ob, reward, done)
			ob, reward, done, _ = self.env.step(action)
			self.env.render()
			if done: break