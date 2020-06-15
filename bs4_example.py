#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 00:02:26 2020

@author: shirishgupta
"""



from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import numpy as np
#import urllib2
import requests

final_data = pd.DataFrame()
for i in range(10):
    
    #url = "https://itunes.apple.com/us/rss/customerreviews/page={}/id=350189835/sortBy=mostrecent/xml".format(i+1)
    url = "https://itunes.apple.com/us/rss/customerreviews/page={}/id=284882215/sortBy=mostrecent/xml".format(i+1)
    
    xml_data = requests.get(url).content

    soup = BeautifulSoup(xml_data, "xml")
     
    
    texts = str(soup.findAll(text=True)).replace('\\n','')
    
    child = soup.find("entry")
    
    Title = []
    content_type = []
    updated = []
    rating = []
    user_name = []
    
    while True:    
        try:
            updated.append(" ".join(child.find('updated')))
        except:
            updated.append(" ")
            
        try:
            Title.append(" ".join(child.find('title')))
        except:
            Title.append(" ")
        
        try:
            content_type.append(" ".join(child.find('content')))
        except:
            content_type.append(" ")
            
        try:
            rating.append(" ".join(child.find('im:rating')))
        except:
            rating.append(" ")
        
        try:
            user_name.append(" ".join(child.find('name')))
        except:
            user_name.append(" ")
        
        try:   
            child = child.find_next_sibling('entry')
        except:
            break
    
    data = []
    data = pd.DataFrame({"updated":updated,
                                    "Title":Title,
                                    "content_type":content_type,
                                    "rating":rating,
                                    "user_name":user_name})
    final_data = final_data.append(data, ignore_index = True)
                                   