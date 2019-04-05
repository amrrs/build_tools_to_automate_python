"""

API Documentation https://github.com/HackerNews/API

"""

import requests

import pandas as pd

top_stories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")

# print(result.content)

base_url = "https://hacker-news.firebaseio.com/v0/item/"

empty_dict = {"title":[], "score":[], "url":[]}

for id in top_stories.json()[0:10]:
    each_story = requests.get(base_url+str(id)+".json?print=pretty").json()
    empty_dict["title"].append(each_story["title"])
    empty_dict["score"].append(each_story["score"])
    empty_dict["url"].append(each_story["url"])

print(pd.DataFrame(empty_dict, index=None))





