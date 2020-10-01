import numpy as np 
import random
class CBT:
	def __init__(self,num_states,num_actions):
		
		self.num_actions=num_actions
		self.num_states=num_states
		self.q=np.zeros((num_states,num_actions))

	def reset(self):
		self.q=np.zeros((self.num_states,self.num_actions))

	def act(self,state,e_rate):
		if(random.random()<e_rate):
			return np.random.randint(self.num_actions)
		else:
			return np.argmax(self.q[state,:])

	def update(self,state,action,reward,e_rate,lr=0.1):
		state=int(state)
		action=int(action)		
		self.q[state,action]+=lr*(reward-self.q[state,action])
		
	def get_policy(self):
		return np.array([np.argmax(self.q[state,:]) for state in range(self.num_states)])