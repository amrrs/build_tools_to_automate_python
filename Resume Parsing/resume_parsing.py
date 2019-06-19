#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
import pdfminer
import re
import os
import pandas as pd


# In[2]:


import pdf2txt


# In[3]:


def convert_pdf(f):

    output_filename = os.path.basename(os.path.splitext(f)[0]) + '.txt'
    #output_filepath = os.path.join('..', 'data', 'output', output_filename)
    output_filepath = os.path.join('output/txt/', output_filename)
    #logging.info('Writing text from {} to {}'.format(f, output_filepath))
    pdf2txt.main(args=[f, '--outfile', output_filepath])
    print(output_filepath + " saved successfully!!!")
    return open(output_filepath).read()


# In[4]:


os.path.splitext("Sally CrookCV.pdf")[0]


# In[5]:


nlp = spacy.load("en_core_web_sm")


# In[6]:


#phone_num credit https://stackoverflow.com/a/3868861


# In[7]:


result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []


# In[8]:


def parse_content(text):
    skillset = re.compile('python|java|sql|hadoop|tableau')
    phone_num = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ is 'PERSON'][0]
    print(name)
    email = [word for word in doc if word.like_email == True][0]
    print(email)
    phone = str(re.findall(phone_num,text.lower()))
    skills_list = re.findall(skillset,text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully!!!")


# In[9]:


for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print('Reading.....' + file)
        txt = convert_pdf(os.path.join('resumes/',file))
        parse_content(txt)


# In[10]:


result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills
#print(result_dict)


# In[11]:


result_df = pd.DataFrame(result_dict)
result_df


# In[12]:


result_df.to_csv('output/csv/parsed_resumes.csv')

