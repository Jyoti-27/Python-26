#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# # Series Concatenation

# In[3]:


ser1=pd.Series(['A', 'B', 'C'], index=[1,2,3])
ser1


# In[7]:


ser2=pd.Series(['D', 'E', 'F'], index=[4,5,6])
ser2


# In[8]:


# Concat() function  for concatenating the series
# stack the series one below the other
print("Concatenated Series is \n", pd.concat([ser1, ser2]))


# In[11]:


ser3=pd.Series(['F', 'G', 'H'], index=[9,10,11])
ser3


# In[12]:


list=[ser1,ser2,ser3]
print(pd.concat(list))


# # DataFrame Concatenation

# In[15]:


df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}) # create DataFrame as a Dictionary of list
df1


# In[18]:


df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}) # create DataFrame as a Dictionary of list
df2


# # Concatenation can be rowwise one DF below another axis=0
# # columns stacked alongside axis=1

# In[19]:


print("Concatenated DataFrame axis=0\n", pd.concat([df1,df2], axis=0))


# In[21]:


print("Concatenated DataFrame axis=1\n", pd.concat([df1,df2], axis=1))


# In[22]:


df3=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}) # create DataFrame as a Dictionary of list
df1


# In[23]:


df4=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'B' :['ear', 'eat', 'egg'], 'C' :['fan', 'fat', 'fog']}) # create DataFrame as a Dictionary of list
df4


# In[25]:


print("Concatenated DataFrame axis=0\n", pd.concat([df3,df4], axis=0))# axis = 0 overlapping is there
# for overlapping columns the values are also stacked below
# concatenation  with axis = 0 considers the overlap of columns


# In[26]:


print("Concatenated DataFrame axis=1\n", pd.concat([df3,df4], axis=1)) # axis = 1 no overlapping
# for overlapping columns the values are also stacked below
# concatenation  with axis = 1 considers the overlap of columns


# In[28]:


print("Concatenated DataFrame axis=0\n", pd.concat([df1,df2], ignore_index=True)) # generated new indexes of DataFrame


# In[29]:


print("Concatenated DataFrame axis=1\n", pd.concat([df1,df2], ignore_index=True))


# In[32]:


df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=0\n", pd.concat([df1,df2], axis=0))


# In[33]:


df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=1\n", pd.concat([df1,df2], axis=1)) #with repeated columns, it will just append the columns and consider common rows


# In[34]:


df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=0\n", pd.concat([df1,df2], ignore_index=True))


# ### Axis=0 
# # Concatenation just appends on DataFrame below another
# # Considers the intersection of columns stacks values for them one below other
# # rowwise indices if there is repeatation it reins the repeatations

# ### Axis=1 
# # Concatenation just appends alongside the other columns are put together
# # Considers the intersection of rows stacks values for them one on the side of the other
# # columns indices(columns name) if there is repeatation it reins the repeatations

# In[36]:


df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=0\n", pd.concat([df1,df2], ignore_index=True))


# In[37]:


# case for no common columns
df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=1\n", pd.concat([df1,df2], axis=1))


# * eg: of two files having common ampides and different columns
# * one file has name and address
# * another file has dept. salary

# In[38]:


# case for common columns
df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[2,3,4]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=1\n", pd.concat([df1,df2], axis=1))


# In[39]:


# case for common rows indices columns
df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[2,3,4]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=1\n", pd.concat([df1,df2], axis=1))


# In[40]:


# case for no common rows indices columns
df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[4,5,6]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=1\n", pd.concat([df1,df2], axis=1))


# In[41]:


# case for no common rows indices columns
df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[4,5,6]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=0\n", pd.concat([df1,df2], axis=0))
# concatenation on axis=0 stacks the rows repeatition of the row is retained, stack the overlappingcolumn values
# concatenation of axis=1 stacks the columns repeatition of the column is retained, stack the overlapping row values


# In[42]:


# case for no common rows indices columns
df1=pd.DataFrame({'A' :['axe', 'art', 'ant'], 'B' :['bat', 'bar', 'bin'], 'C' :['cat', 'cap', 'car']}, index=[1,2,3]) # create DataFrame as a Dictionary of list
df2=pd.DataFrame({'D' :['dog', 'den', 'dot'], 'E' :['ear', 'eat', 'egg'], 'F' :['fan', 'fat', 'fog']}, index=[4,5,6]) # create DataFrame as a Dictionary of list
print(df1)
print(df2)
print("Concatenation DataFrames axis=1\n", pd.concat([df1,df2], axis=1))
# concatenation on axis=0 stacks the rows repeatition of the row is retained, stack the overlappingcolumn values
# concatenation of axis=1 stacks the columns repeatition of the column is retained, stack the overlapping row values


# In[ ]:


## Merge is based on common columns


# In[44]:


df_stud = pd.DataFrame({'St_id' :[101, 102,103,104,105], 'Branch' :['IT', 'CS', 'ECE', 'CS', 'MECH']})
df_stud


# In[49]:


df_fac = pd.DataFrame({'F_id' :[110, 120,130,140,150],'F_name' :['A', 'B', 'C', 'D', 'E'], 'Branch' :['ECE', 'MECH', 'EEE', 'IT', 'CS']})
print("Student DataFrame:\n", df_stud, '\n Faculty DataFrame :\n', df_fac)


# In[50]:


df_fac = pd.DataFrame({'F_id' :[110, 120,130,140,150],'F_name' :['A', 'B', 'C', 'D', 'E'], 'Branch' :['ECE', 'MECH', 'EEE', 'IT', 'CS']})
print("Student DataFrame:\n", df_stud, '\n Faculty DataFrame :\n', df_fac)
df_fac


# In[51]:


df_fac = pd.DataFrame({'F_id' :[110, 120,130,140,150],'F_name' :['A', 'B', 'C', 'D', 'E'], 'Branch' :['ECE', 'MECH', 'EEE', 'IT', 'CS']})
print("Student DataFrame:\n", df_stud, '\n Faculty DataFrame :\n', df_fac)
df_fac
print(pd.concat([df_stud,df_fac], axis=1))


# In[52]:


df_fac = pd.DataFrame({'F_id' :[110, 120,130,140,150],'F_name' :['A', 'B', 'C', 'D', 'E'], 'Branch' :['ECE', 'MECH', 'EEE', 'IT', 'CS']})
print("Student DataFrame:\n", df_stud, '\n Faculty DataFrame :\n', df_fac)
df_fac
print(pd.merge(df_stud,df_fac,on='Branch', sort=True))


# In[54]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd'],'data2' :[3,6,9]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)


# In[57]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd'],'data2' :[3,6,9]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Outer Join :\n", pd.merge(df1,df2,on='key', how='outer', sort=True))  # union of keys


# In[60]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd'],'data2' :[3,6,9]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Inner Join :\n", pd.merge(df1,df2,on='key', how='inner', sort=True))  # intersection of keys


# In[62]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)


# In[69]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Left Join :\n", pd.merge(df1,df2,on='key', how='left', sort=True))  # keys of let dataframe


# In[68]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Right Join :\n", pd.merge(df1,df2,on='key', how='right', sort=True))  # keys from right dataframe


# In[63]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Outer Join :\n", pd.merge(df1,df2,on='key', how='outer', sort=True))  # union of keys


# In[64]:


df1=pd.DataFrame({'key' :['b', 'a', 'd', 'e'], 'data1' :[0,4,6,8]})  # has unique
df2=pd.DataFrame({'key' :['a', 'b', 'd', 'f'],'data2' :[3,6,9,11]}) # has unique row labels
print("DataFrame1 :\n", df1, '\n DataFrame2 :\n',df2)
print("Inner Join :\n", pd.merge(df1,df2,on='key', how='inner', sort=True))  # intersection of keys


# ### Summary of the above
# #### One One join with four cases outer, inner, left and right

# In[4]:


#many one merge
df1=pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a','a'], 'data1':[10,20,30,40,50,60]})
df2=pd.DataFrame({'key':['a', 'b', 'd'], 'data2':[100, 200, 300]})
print("\n", df1)
print("\n", df2)
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# union of keys 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))    
# intersection of keys 
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))  
#  keys from left dataframe
print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))   
#  keys from right  dataframe


# In[5]:


#many one merge
df1=pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a','a'], 'data1':[10,20,30,40,50,60]})
df2=pd.DataFrame({'key':['a', 'b', 'd'], 'data2':[100, 200, 300]})
print("\n", df1)
print("\n", df2)
print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# union of keys 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))    
# intersection of keys 
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))  
#  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))   
#  keys from right  dataframe


# In[6]:


#many one merge
df1=pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a','a'], 'data1':[10,20,30,40,50,60]})
df2=pd.DataFrame({'key':['a', 'b', 'd'], 'data2':[100, 200, 300]})
print("\n", df1)
print("\n", df2)
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# union of keys 
print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))    
# intersection of keys 
#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))  
#  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))   
#  keys from right  dataframe


# In[7]:


#many one merge
df1=pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a','a'], 'data1':[10,20,30,40,50,60]})
df2=pd.DataFrame({'key':['a', 'b', 'd'], 'data2':[100, 200, 300]})
print("\n", df1)
print("\n", df2)
#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# union of keys 
#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))    
# intersection of keys 
print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))  
#  keys from left dataframe
#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))   
#  keys from right  dataframe


# In[8]:


# Many many merge
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a'], 'data1': [10,20,30,40,50,60]})  
#has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'b', 'a', 'd'], 'data2': [100,200,300,400,500]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to many  merge situation
#No of rows in the dataframe = 6x5 for outer

print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# Union of keys 

#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))   
# Intersection of keys

#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))    
#  keys from left dataframe

#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[9]:


# Many many merge
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a'], 'data1': [10,20,30,40,50,60]})  
#has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'b', 'a', 'd'], 'data2': [100,200,300,400,500]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to many  merge situation
#No of rows in the dataframe = 6x5 for outer

#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# Union of keys 

print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))   
# Intersection of keys

#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))    
#  keys from left dataframe

#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[10]:


# Many many merge
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a'], 'data1': [10,20,30,40,50,60]})  
#has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'b', 'a', 'd'], 'data2': [100,200,300,400,500]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to many  merge situation
#No of rows in the dataframe = 6x5 for outer

#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# Union of keys 

#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))   
# Intersection of keys

print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))    
#  keys from left dataframe

#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[11]:


# Many many merge
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a'], 'data1': [10,20,30,40,50,60]})  
#has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'b', 'a', 'd'], 'data2': [100,200,300,400,500]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to many  merge situation
#No of rows in the dataframe = 6x5 for outer

#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# Union of keys 

#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))   
# Intersection of keys

print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))    
#  keys from left dataframe

#print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[12]:


# Many many merge
df1 =pd. DataFrame({'key' : ['b', 'b', 'a','c', 'a', 'a'], 'data1': [10,20,30,40,50,60]})  
#has multiple rows labelled a and b
df2 = pd.DataFrame({'key' : ['a', 'b', 'b', 'a', 'd'], 'data2': [100,200,300,400,500]})
print("DataFrame1 : \n", df1, '\nDataFrame2 :\n', df2)

#Example of many to many  merge situation
#No of rows in the dataframe = 6x5 for outer

#print("Outer Join:\n", pd.merge(df1, df2, on ='key', how = 'outer', sort=True))   
# Union of keys 

#print("Inner Join:\n", pd.merge(df1, df2, on ='key', how = 'inner', sort=True))   
# Intersection of keys

#print("Left Join:\n", pd.merge(df1, df2, on ='key', how = 'left', sort=True))    
#  keys from left dataframe

print("Right Join:\n", pd.merge(df1, df2, on ='key', how = 'right', sort=True))     # 
#Here left and outer is same and Right and Inner is same


# In[ ]:





# In[ ]:





# In[ ]:




