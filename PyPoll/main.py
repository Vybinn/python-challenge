#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies 
import pandas as pd
import os
import csv
import numpy as np


# In[2]:


#specify filepath
pollpath = os.path.join("Resources", "election_data.csv")


# In[3]:


#open csv and read 
pollpathpd=pd.read_csv(pollpath)
pollpathpd.head()


# In[4]:


#find the total number of votes based on number of unique IDs
numvotes=(len(pollpathpd["Voter ID"].unique()))
numvotes


# In[5]:


#get a list of the candidates by scrubbing candidate list for unique names
candidates = pollpathpd["Candidate"].unique()
candidates


# In[6]:


#Tally the total number of votes for each candidate
candcount = pollpathpd["Candidate"].value_counts()
candcount


# In[7]:


#Determine the percent of the overall votes each candidate received
candper = candcount / numvotes * 100
candper


# In[8]:


#determine the winner based on the candidated that received the most number of votes
winner = pollpathpd["Candidate"].mode()


# In[9]:


#create a data frame with the summary info
summary_polls_dicts = {"Candidates": ["Khan", "Correy", "Li", "O'Tooley"], 
                              "Percent of Vote": ["63%", "20%", "14%", "3%"],
                              "Total Votes": ["2,218,231", "704,200", "492,940", "105,630"]}
summary_polls_df=pd.DataFrame(summary_polls_dicts)
summary_polls_df


# In[10]:


#set up print statement to identify winner
print ("Winner is " + (winner))


# In[14]:


#assigned variables for each individual data point, in order to be able to print them within this script and embed
#them in text files without indices, controlling for spacing, etc. This step is not necessary, but it allowed me 
#to better control the spacing and layout of the print statements
Kname = summary_polls_df.iloc[0,0]
Kper = summary_polls_df.iloc[0,1]
Kvotes = summary_polls_df.iloc[0,2]
Cname = summary_polls_df.iloc[1,0]
Cper = summary_polls_df.iloc[1,1]
Cvotes = summary_polls_df.iloc[1,2]
Lname = summary_polls_df.iloc[2,0]
Lper = summary_polls_df.iloc[2,1]
Lvotes = summary_polls_df.iloc[2,2]
Oname = summary_polls_df.iloc[3,0]
Oper = summary_polls_df.iloc[3,1]
Ovotes = summary_polls_df.iloc[3,2]


# In[15]:


#Assigned variables to each line in the statement. Again, this step is not necessary, but allowed for better control
#in the layout and spacing of the print statements without indices in this file and in accompaying txt file
a = ("Election Results")
b = ("---------------------------")
c = ("Total Votes: " + str(numvotes))
d = ("---------------------------")
e = (Kname +":     "  +  Kper  +" " + Kvotes)
f = (Cname +":   "  +  Cper  +" " + Cvotes)
g = (Lname +":       "  +  Lper  +" " + Lvotes)
h = (Oname +": "  +  Oper  +"  " + Ovotes)
m = ("---------------------------")
n = ("Winner is " + Kname)
o = ("---------------------------")
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)
print (h)
print (m)
print (n)
print (o)

     


# In[16]:


#created and opened a writeable text file
file1 = open("PyPolls_Summary.txt", "w+")


# In[17]:


#populated text file with the results of the election, layed out in the format above, with information on different lines. 
#This is a longer way of printing results, but allows for better control in the layout and spacing of info in 
#the text file. 
file1.write("This is Craig Hall's summary of PyPolls \n")
file1.write(a + " \n")
file1.write(b + " \n")
file1.write(c + " \n")
file1.write(d + " \n")
file1.write(e + " \n")
file1.write(f + " \n")
file1.write(g + " \n")
file1.write(h + " \n")
file1.write(m + " \n")
file1.write(n + " \n")
file1.write(o + " \n")
file1.close()


# In[ ]:




