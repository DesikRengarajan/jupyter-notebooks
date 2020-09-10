import numpy as np 
import random 
import math 

class news:
	def __init__(self,actions,num_users=10):
		self.num_users=num_users		
		self.actions=actions
		self.num_actions=len(actions)
		self.users=[i for i in range(num_users)]
		self.actions_i=[i for i in range(len(actions))]
		self.tod=[i for i in range(24)]
		self.location=[i for i in range(10)]

	def get_context(self):
		u=np.random.choice(self.users)
		t=np.random.choice(self.tod)
		l=np.random.choice(self.location)
		i=np.random.random(self.num_actions)
		i=i/sum(i)		
		context={'user': u, 'time_of_day': t,"location":l,"interest":list(i)}
		return context

	def get_cost(self,context,action_i):
		reward=0.0		
		if(context['user']%2==0 and context['time_of_day']%4==0 and context['location']%3==0):
			a=np.random.choice(self.actions_i,p=context['interest'])
			if(action_i==a):
				reward=-1.0
			return reward
		if(context['user']%3==0 and context['time_of_day']%3==0):
			a=np.random.choice(self.actions_i,p=context['interest'])
			if(action_i==a):
				reward=-1.0
			return reward

		if(context['user']%5==0):
			a=np.random.choice(self.actions_i,p=context['interest'])
			if(action_i==a):
				reward=-1.0
			return reward

		if(context['user']%7==0):
			a=np.random.choice(self.actions_i,p=context['interest'])
			if(action_i==a):
				reward=-1.0
			return reward

		else:
			return reward


class simple_news:
	def __init__(self,num_users=10,num_actions=5):
		self.num_actions=num_actions
		self.num_users=num_users
		self.actions=[i for i in range(self.num_actions)]
		self.users=[i for i in range(self.num_users)]
		self.tod=[i for i in range(24)]

	def get_context(self):
		u=np.random.choice(self.users)
		t=np.random.choice(self.tod)
		context={'user':u,'tod':t}
		return context 

	def get_cost(self,context,action):
		u=int(context['user'])
		t=int(context['tod'])
		
		if ((u==0) and (t<5)):
			if(action%2==0):
				return -1.0
		if ((u%3==0) and (t<15)):
			if(action%2==0):
				return -1.0
		if ((u==1) and (t<20)):
			if(action%3!=0):
				return -1.0
		if ((u%2==0) and (t<12)):
			if(action==1):
				return -1.0
		if ((u%2==0) and (t<20)):
			if(action==3):
				return -1.0
		if ((u==5) and (t<20)):
			if(action==4):
				return -1.0
		if ((u==7) and (t<20)):
			if(action==4):
				return -1.0
		
		return 0.0					


		












