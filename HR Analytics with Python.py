#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df1 = pd.read_csv('people.csv')


# In[5]:


df1


# In[34]:


df.head()


# In[35]:


df.info()


# In[ ]:





# In[ ]:


#statistical analysis


# In[8]:


df1.describe()


# In[6]:


df1.isna().sum() - #Null Values


# In[ ]:


#Remove Duplicates


# In[7]:


df1 = df1.drop_duplicates()


# In[8]:


df1.describe()


# In[9]:


df1


# In[10]:


col=['satisfactoryLevel','lastEvaluation','numberOfProjects','avgMonthlyHours',
     'timeSpent.company','workAccident','left','promotionInLast5years']


# In[12]:


correlation= df1[col].corr()


# In[13]:


correlation


# In[14]:


sns.heatmap(correlation, annot = True)


# In[ ]:


#Total Attrition Rate of Company


# In[15]:


sns.countplot(x=df1['left'], hue=df1['left'])
plt.title('Plot 1 - Attrition Rate Count')


# In[ ]:


#Count of people who leave the company


# In[11]:


df1['left'].value_counts()


# In[27]:


#Percentage of People Staying and Leaving
plt.pie(x=list(df1['left'].value_counts()), labels=['Staying', 'Leaving'], startangle = 90,autopct='%.2f%%')
plt.title('PLot 2 Percentage of People Staying and Leaving')


# In[ ]:


#According to the above analysis, 83% Employees are staying and 17% of Employees are leaving
#which is obviously a higher rate of attrition rate


# In[26]:


#Analysis based on project number. Whether there is an impact of number of project handled by an employee and them leaving.

sns.countplot(x=df1['numberOfProjects'], hue=df1['left'])
plt.xlabel('No of Projects per Employee')
plt.title('PLot 3 Employee-Project Count Graph')


# In[ ]:


#Above analysis clearly shows that people with lower number of projects i.e less than 3 
#and also employees with more than 5 projects are leaving the company.


# In[43]:


#now let us see what is attrition rate for employess with either less projects or more projects

less_project = len(df1[(df1['numberOfProjects']<3) & (df1['left']==1)])
print('Less Projects and Leaving :',less_project)
print('Less Project and Leaving Percentage :', less_project/11991*100)
more_projects = len(df1[(df1['numberOfProjects']<5) & (df1['left']==1)])
print('More projects and Leaving :',more_projects)
print('More Project and Leaving Percentage :', more_projects/11991*100)


# In[ ]:


#Above analysis clearly shows that people with lower number of projects i.e less than 3 
#and also employees with more than 5 projects are leaving the company.


# In[51]:


#Analysis based on Work Accidents.

sns.countplot(x=df1['workAccident'], hue=df1['left'])
plt.xlabel('No of Employees with Work Accidents & Leaving')
plt.title('Plot: 4 Attrition based on Work Accidents & Leaving')


# In[49]:


#now let us see what is attrition rate for employess with work accident and without work accident

no_wa= len(df1[(df1['workAccident']==0) & (df1['left']==1)])
print('no work accident, but leaving: ',no_wa)
print('percentage: ', (no_wa/11991)*100)

#work accident and leaving
wa_l= len(df1[(df1['workAccident']==1) & (df1['left']==1)])
print('work accident and leaving: ',wa_l)
print('percentage: ', (wa_l/11991)*100)


# In[16]:


df1['dept'].unique()


# In[18]:


#Analysis based on department.

sns.countplot(x=df1['dept'],hue=df1['left'])
plt.title('Plot: 5 Attrition in Each department')
plt.xticks(rotation=90)


# In[ ]:


# Highest number of people leave from Sales and technical departments.


# In[19]:


df1.groupby(by='dept').sum()['left'].sort_values(ascending=True)


# In[21]:


#together for attrition rate of all departments:

for col in df1['dept'].unique():
  var=len(df1[(df1['dept']==col) & df1['left']==1])
  print('attrition rate: ', (var/11991)*100, 'for ',col)


# In[22]:


# If there is relation between Salary and Attrition Rate


# In[23]:


sns.countplot(x=df1['salary'],hue=df1['left'])
plt.title('Plot: 6 Attrition based on Salary')


# In[25]:


#attrition rate of employess with low salary and leaving
low= len(df1[(df1['salary']=='low') & (df1['left']==1)])
print('percentage of employess with low salary and leaving: ', (low/11991)*100)

#attrition rate of employess with low salary and leaving
med= len(df1[(df1['salary']=='medium') & (df1['left']==1)])
print('percentage of employess with medium salary and leaving: ', (med/11991)*100)

#attrition rate of employess with low salary and leaving
high= len(df1[(df1['salary']=='high') & (df1['left']==1)])
print('percentage of employess with high salary and leaving: ', (high/11991)*100)


# In[ ]:




