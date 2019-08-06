
# coding: utf-8

# In[1]:


# Imports
import random
from matplotlib import pyplot as plt


# In[2]:


class Agent():
    '''
    The class defining the main characteristics of my agents
    '''
    def __init__ (self, patient, belief, money = 0):
        '''
        To begin, all agents are patient, they have some belief and 0 money
        '''
        self.patience = patient
        self.money = money 
        self.beliefs = belief
    


# In[40]:


class Model():
    '''
    The bank run mechanism is outlined in this class.
    '''
    def __init__(self, N , belief, max_iterations=100, total_reserves = 10000):
        
        self.N = N #Agent population
        self.beliefs = belief #Agents degree of confidence (i.e. belief in system)
       
    
        #The following are lists to capture some output
        self.impatient_agents = list() 
        self.reserves_history = list()
        
        ''' 
        Here I'm constructing a list of ALL agents, they begin patient and are assigned some random degree of belief (above 0.5).
        The higher the belief value the higher degree of confidence the agent begins with
        '''
        self.agents = list()
        for i in range(N):
            self.beliefs = (random.random()) 
            self.agents.append(Agent(True, belief = random.random()*0.5 + 0.5))
        
        # Make a variable to keep track of the number of impatient people
        impatient_agents = list() 
        for agent in self.agents:
            if agent.patience == False:
                impatient_agents.append(agent) # Adding them to the impatient_agenys list above
        self.num_of_impatients = len(impatient_agents)
        
        
        # Keep a record of the model time
        self.time = 0
        
        # Note down the max iterations
        self.max_iterations = max_iterations
        
        # Total bank reserves, we assume the bank has 10,000 money units liquid
        self.total_reserves = total_reserves
        
        # Agents perception rates
        self.alpha1 = 0.008
        self.alpha2 = 0.02
        
   
    def run(self):
        '''
        This function runs the model.
        '''
        for t in range(self.max_iterations):
            if random.random() > 0.5:
                qual_info = (random.random()) # Some random degree of bad quality information will be broadcasted at random time periods
            else:
                pass
            '''
            In every timestep, for every patient agent (every agent), assuming  quality of bad information is greater than 0.5,
            their peception of the bad news reduces their degree of confidence by alpha 0.02 (large amount).
            '''
            for agent in self.agents:
                if agent.patience == True:
                    if qual_info >= 0.5:
                        agent.beliefs -= self.alpha2
                    else: 
                        '''
                        If the quality of bad information is less than 0.5, the perception is relatively smaller (alpha = 0.008)
                        '''
                        agent.beliefs -= self.alpha1
                else:
                    '''
                    And, regardless of the quality of information broadcasted, their belief still reduces by alpha 0.02. 
                    '''
                    agent.beliefs -= self.alpha2
                
                if agent.patience == True:
                    '''
                    Following this, if agents still remain patient:
                    if they observe that 0.66 of the population are impatient or that agents beliefs are less than 0.5,
                    they become impatient
                    '''
                    if self.num_of_impatients > self.N/1.5 or agent.beliefs <= 0.5:
                        agent.patience = False
                 
                if agent.patience == False:
                    '''
                    Based on this transition to impatient(from patient) agents withdraw their funds from the bank, assuming the bank is liquid.
                    '''
                    agent.money +=1
                    if self.total_reserves > 0:
                        self.total_reserves -= 1
            
            # To keep track of bank reserves
            self.reserves_history.append(self.total_reserves)
            
        
            # Update model time
            self.time += 1
            # This variable updates the impatient list every timestep
            impatient_agents = list()
            
            for agent in self.agents:
                if agent.patience == False:
                    impatient_agents.append(agent)
                    self.num_of_impatients = len(impatient_agents)
            self.impatient_agents.append(self.num_of_impatients)
            
            print("Time period: ", self.time)
            print("Quality of information: ", qual_info)
            print("Number of impatient people: ", self.num_of_impatients)
    


# In[41]:


# Initialising the model with 100 agents and 0 degree of belief
m = Model(100, 0)


# In[42]:


# Checking my agents attributes: they all begin patient, have some degree of confidence (above 0.5) and have no money. 
for agent in m.agents:
    print(agent.patience, agent.beliefs, agent.money)


# In[45]:


m.run()


# In[49]:


# Visualising the number of impatient agents
timestep_no = range(len(m.impatient_agents))
plt.figure(figsize=(15,10))
plt.bar(timestep_no, m.impatient_agents)
plt.ylabel('Number of Impatient Agents')
plt.xlabel('Time Periods')
plt.title('Transition from Patient to Impatient Agents')
plt.show()


# In[18]:


# Visualising bank reserves rate of depletion over time
timesteps = range(len(m.reserves_history))
plt.figure(figsize=(15,10))
plt.bar(timesteps, m.reserves_history)
plt.ylabel('Bank Reserves')
plt.xlabel('Time Periods')
plt.title('Bank Run: The depletion of Reserves over time')
plt.show()


# In[17]:


'''To check banks reserves decrease'''
# print(m.reserves_history) 

