#!/usr/bin/env python
# coding: utf-8

# # 

# In[1]:


# 使用requests实现post请求


# In[2]:


import requests


# In[3]:


r = requests.get('http://www.tmall.com')


# In[4]:


print(r.encoding)  # utf-8


# In[5]:


print(type(r.headers))


# In[6]:


print(r.headers['Content-type'])  # text/html; charset=utf-8


# In[ ]:





# In[7]:


# 设置请求头部信息模拟浏览器访问


# In[8]:


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"}


# In[9]:


html = requests.get('http://www.tmall.com', headers = headers)


# In[10]:


html.status_code


# In[11]:


html.content


# In[12]:


html.text


# In[ ]:





# In[13]:


# 设置使用代理ip


# In[14]:


proxies = {'http':'https://122.72.32.73:80',
          'http':'https://58.67.159.50:80', } # Python 3.7 开始 https://需要被添加


# In[15]:


html = requests.get('http://www.tmall.com', headers = headers, proxies = proxies)


# In[ ]:


html.text


# In[ ]:




