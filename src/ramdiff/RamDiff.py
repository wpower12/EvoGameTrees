import gym

ITERATIONS = 200
RAM_SIZE = 128

class RandomAgent(object):
	def __init__(self, action_space):
		self.action_space = action_space

	def act(self, observation, reward, done):
		return self.action_space.sample()

def get_ranked_ram_locs( env_name ):
	print("generating ranked ram list")
	env = gym.make(env_name)
	agent = RandomAgent(env.action_space)
	change_count = [ 0 for i in range(RAM_SIZE) ]
	frame_0, frame_1 = [], []
	done = False
	reward = 0
	ob = env.reset()
	frame_0 = ob
	frame_1 = ob

	for j in range(ITERATIONS):
		action = agent.act(ob, reward, done)
		ob, reward, done, _ = env.step(action)
		frame_1 = ob
		diff = frame_1 - frame_0
		diff = [0 if d == 0 else 1 for d in diff]
		frame_0 = frame_1
		change_count = [i+j for i,j in zip(change_count, diff)]
		if done: break

	sorted_locations = [i[0] for i in sorted(enumerate(change_count), key=lambda x:x[1])]
	return list(reversed(sorted_locations))
