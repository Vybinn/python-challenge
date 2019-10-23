#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import dependencies
import pandas as pd
import os


# In[3]:


#specify path of data source file
banks = os.path.join("Resources", "budget_data.csv")


# In[4]:


#read the csv file
databanks = pd.read_csv(banks)


# In[5]:


#check / view a sample of the data
databanks.head()


# In[6]:


#determine the total number of months in the analysis
totmonths = len(databanks["Date"].unique())
totmonths


# In[7]:


#determine the overall profit/loss by taking a sum of all profits and losses
pl = databanks["Profit/Losses"].sum()
pl


# In[8]:


#deatermine the average of all profits and losses
avg = databanks["Profit/Losses"].mean()
avg


# In[9]:


#round the average to the nearest cent
round_avg = round((avg),2)
round_avg


# In[10]:


#determine the greatest increase in a single month by looking for the max value
bestinc = databanks["Profit/Losses"].max()
bestinc


# In[11]:


#determine the index of the greatest increase to locate full information for the entry
bestincind = databanks["Profit/Losses"].argmax()
bestincind


# In[12]:


#determine the worst loss by looking at the minimum value in profits / losses
worstdec = databanks["Profit/Losses"].min()
worstdec


# In[13]:


#locate the index of the worst loss to find full information related to the loss
worstdecind = databanks["Profit/Losses"].argmin()
worstdecind


# In[14]:


#printed indexes of best and worst to determine the dates on which they happened
print(databanks.iloc[[25,44]])


# In[15]:


#assigned variables for the dates of the best increase and worst loss
best_month = databanks.iloc[25,0]
worst_month = databanks.iloc[44,0]
print (best_month)
print (worst_month)


# In[16]:


#assigned variables for each line that I wanted to print in this file and the accompanying text file.  
#It was not necessary to compile the data like this, but allowed for greater flexibility in controlling 
#the layout, spacing and positions of the information I wanted to print.  
a=("Financial Analysis")
b=("---------------------")
c=("Total Months: " + str(totmonths))
d=("Total: $" + str(pl))
e=("Average Change: $" + str(round_avg))
f=("Greatest Increase in Profits: " + best_month + "  $" + str(bestinc))
g=("Greatest Decrease in Profits: " + worst_month + "  $" + str(worstdec))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)


# In[17]:


#created data frame of the summary information
banksummary = pd.DataFrame({"Total Months": [totmonths], "Total Profits/Losses": str(pl), "Average Change": str(round_avg), "Greatest Increase in Profits": best_month + " $" +str(bestinc), "Greatest Decrease in Profits": worst_month + " $" +str(worstdec)})
banksummary


# In[18]:


#opened a writeable txt file to contain a printout of the summary data
file1 = open("PyBanks_Summary.txt", "w+")


# In[19]:


#wrote the individual lines summarizing the key data.  Again, it is not necessary to compile it with this many 
#steps, but allowed for greater flexibility in spacing and layout.  Closed the file. 
file1.write("This is Craig Hall's summary of PyBanks \n")
file1.write(a + " \n")
file1.write(b + " \n")
file1.write(c + " \n")
file1.write(d + " \n")
file1.write(e + " \n")
file1.write(f + " \n")
file1.write(g + " \n")
file1.close()


# In[ ]:




