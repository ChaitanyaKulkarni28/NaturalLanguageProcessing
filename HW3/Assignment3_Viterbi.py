
# coding: utf-8

# In[26]:


import sys


# In[27]:


viterbi = {}
backpointer = {}

states = ["HOT","COLD"]
initial_probablity = {"HOT": 0.8, "COLD": 0.2}

stateSeq = []

transition_probabilities = {("HOT","HOT"):0.7, ("HOT","COLD"):0.3, ("COLD","HOT"):0.4, ("COLD","COLD"):0.6}
observation_likelihoods = {(1,"HOT"):0.2, (2,"HOT"):0.4 , (3,"HOT"):0.4, (1,"COLD"):0.5, (2,"COLD"):0.4, (3,"COLD"):0.1}

observationSeq = sys.argv[1]
observations = [int(s) for s in observationSeq]


# In[28]:


viterbi[("HOT",0)] = initial_probablity["HOT"] * observation_likelihoods[(observations[0],"HOT")]
viterbi[("COLD",0)] = initial_probablity["COLD"] * observation_likelihoods[(observations[0],"COLD")]
backpointer[("HOT",0)] = 0
backpointer[("COLD",0)] = 0


# In[29]:


for observation in range(1,len(observations)):
    prob1 = viterbi[("HOT",observation-1)] * transition_probabilities[("HOT","HOT")] * observation_likelihoods[(observations[observation],"HOT")]
    prob2 = viterbi[("COLD",observation-1)] * transition_probabilities[("COLD","HOT")] * observation_likelihoods[(observations[observation],"HOT")]
    
    viterbi[("HOT",observation)] = max(prob1,prob2)
    
    if prob1 > prob2:
        backpointer[("HOT",observation)] = "HOT"
    else:
        backpointer[("HOT",observation)] = "COLD"
        
    prob3 = viterbi[("COLD",observation-1)] * transition_probabilities[("COLD","COLD")] * observation_likelihoods[(observations[observation],"COLD")]
    prob4 = viterbi[("HOT",observation-1)] * transition_probabilities[("HOT","COLD")] * observation_likelihoods[(observations[observation],"COLD")]
    
    viterbi[("COLD",observation)] = max(prob3,prob4)
    
    if prob3 > prob4:
        backpointer[("COLD",observation)] = "COLD"
    else:
        backpointer[("COLD",observation)] = "HOT"


# In[30]:



lastHot = viterbi[("HOT",len(observations)-1)]
lastCold = viterbi[("COLD",len(observations)-1)]

if lastHot > lastCold:
    stateSeq.append("HOT")
    maxS = "HOT"
else:
    stateSeq.append("COLD")
    maxS = "COLD"
    
for i in range(0,len(observations)-1):
    stateSeq.append(backpointer[(maxS,len(observations)-i-1)])
    maxS = backpointer[maxS,len(observations)-i-1]


# In[31]:


print(list(reversed(stateSeq)))

