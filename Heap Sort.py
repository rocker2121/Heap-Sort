#!/usr/bin/env python
# coding: utf-8

# In[32]:


l=[4,10,3,5,1,8,9,1,0]


# In[6]:


l[5],l[6] =2,3


# In[8]:


l[2*3 +1]


# In[51]:


l


# In[50]:


l[0],l[-1]=l[-1],l[0]


# In[58]:


class heap_sort:
    def __init__(self,lst):
        self.lst=lst
    def _node_eval (self,x=0,leftx=0,rightx=0):
        if (max([x,leftx,rightx])==x):
            return x,leftx,rightx
        elif (max([x,leftx,rightx])==leftx):
            return leftx,x,rightx
        else:
            return rightx,leftx,x
    
    def heaping(self):
        q=[]
        while (len(self.lst)>1):
            
            N=len(self.lst)//2
            N-=1
            
            for i in range(N,-1,-1):
                try:
                    self.lst[i],self.lst[2*i+1],self.lst[2*i+2]=self._node_eval(self.lst[i],self.lst[2*i+1],self.lst[2*i+2])
                except:
                    self.lst[i],self.lst[2*i+1]=self._node_eval(self.lst[i],self.lst[2*i+1],0)[0],self._node_eval(self.lst[i],self.lst[2*i+1],0)[1]
                    
            q.append(self.lst[0])
            self.lst.pop(0)
            self.lst[0],self.lst[-1]=self.lst[-1],self.lst[0]
        q.append(self.lst[0])
        
        return (q)


# In[59]:


l=[4,10,3,5,1,8,9,1,0,60,90,800,87]


# In[60]:


x=heap_sort(l)


# In[61]:


x.heaping()


# In[35]:


l


# In[46]:


l.pop(0)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




