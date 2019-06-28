#!/usr/bin/env python
# coding: utf-8

# # News Extraction

# ### Import Packages

# In[1]:


from bs4 import BeautifulSoup
from requests import get


# ### CLI

# In[48]:


import sys #for argument parsing

# Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the  URL")


# ### Creating a Function to Extract only Text from `<p>` Tags

# In[17]:


def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 #text = soup.text
 title = ' '.join(soup.title.stripped_strings)
 return title , text    


# ### Calling the function with the desired News URL

# In[18]:


#url = "https://en.wikinews.org/wiki/Global_markets_plunge"


# In[19]:


text = get_only_text(url)


# In[26]:


#len(text[1])


# In[27]:


#text[1]


# ### Number of Words - Original Text

# In[28]:


#text[0]


# In[30]:


#len(str.split(text[1]))


# # Summarization

# In[36]:


from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords


# ### Printing the Summarized Text
# 
# ### Method #1 - Word Count

# In[35]:


#text[1]


# In[37]:


print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))


# In[52]:


print("\n\nLength of the summarized text: " + str(len(str.split((summarize(repr(text[1]), word_count=100))))))


# ### Number of Words - Summarized Text

# In[42]:


#print ("Title : " + text[0])
#print ("Summary : ")
#print (summarize(repr(text[1]), ratio=0.1))


# In[43]:


summarized_text = summarize(repr(text[1]), ratio=0.1)


# ### Number of Words - Summarized Text

# In[44]:


#len(str.split(summarized_text))


# ### Keywords

# In[47]:


#print ('\nKeywords:')
#print (keywords(text[1], ratio=0.1, lemmatize=True))


# In[16]:




