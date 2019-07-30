#!/usr/bin/env python
# coding: utf-8

# In[7]:


from random import random
import math
import pylab
import numpy as np


# In[ ]:


scale = [1,20]
patient_agts = 5
impatient_agts = 5 
withdrawal_list = []


# In[ ]:


class Agent(): 
    
    def __init__(self, cash=0):
        self.money = cash
        
    def timestep(self, agents):
        while len(withdrawal_list) > 1:
            withdrawal_list.append(Impatient.decision(cash, decision))
        
    def withdraw(self, cash):
        if self.cash += 1:
            


# In[12]:


class Patient(Agent):
    
    def __init__(self, cash, decision):
        self.money = cash
        self.scale = decision
        self.agentlist = withdraw_list

    def timestep(self):
        """
        Every timestep 'something' happens
        """
        for i in range(len(self.agentlist)):
            self.decision()
            self.scale()
        
    def decision(self, scale, cash):
        if self.scale >= 8:
            self.cash =+ 1
    
    def scale(self, withdraw, quality):
        if i in range(len(self.withdraw)) >= 4:
            self.scale += 1
        else:
            pass
        if self.quality() >= 5: 
            self.scale += 1
        else: 
            pass
    
    def withdraw(self, withdrawal_list, scale):
        """
        If list of withdrawals gets to 4, patient agent withdraws
        """
        if i in range(len(self.withdrawals_list)) >= 4:
            self.scale += 1
        else:
            pass
        
    def information(self, scale):
        """
        Assuming only bad news exists, information is less likely to pressure patient agents independent of
        number of withdrawals
        """
        if random.random() >= 0.5: 
            self.quality += 1
        else: 
            pass
    


# In[ ]:


class Impatient(Agent):
    
    def __init__(self, money, agentlist, decision, update):
        self.otheragents = agentlist
        self.scale = decision_scale
        self.up = update
        self.agent_type = agent_type
        self.money = money
        
    def timestep(self):
        """
        Every timestep 'something' happens
        """
        for i in range(len(self.agentlist)):
            self.decision()
            self.information()
        
    def decision(self, scale):
        """
        If agents scale falls below 10, they withdraw
        """
        if self.scale < 10:
            self.money += 10
        else:
            pass
            
    def scale(self, impatient_agents):
        self.impatient_agents = withdrawal_list
        
        for i in range(len(withdrawal_list)):
            if i >= 5:
            self.scale -=1
        else:
            pass
        
    def information(self, occurance):
        """
        Assuming only bad news exists
        """
        if random.random() >= 0.5: 
            self.occurance == 1
        else: 
            pass


# In[14]:


class Bank():
    
    def __init__(self, reserves = 10):
        self.liquid_assets = reserves
        
    def withdrawals(self):
        self.reserves -= 1
    
    def timestep(self):
        if self.reserves > 0:
            self.reserves -= 1


# In[ ]:




