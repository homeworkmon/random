#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:59:23 2021

@author: monica
"""
import feedparser
import re

xml_file = feedparser.parse('/home/monica/Documents/Python/XML/Donor.xml')

for i, entry in enumerate(xml_file.entries):
    
    title = xml_file.entries[i]['title']
    
    title = title.replace("/", "-") #remove / that confuses file path
    
    content = xml_file.entries[i]['content'][0]['value']
    
    content = content.replace("<span>","<p>") #replace spans w p tag
    content = content.replace("</span>","</p>")
    
    article = re.sub(r"<!--(.*?)-->",'', content) #remove xml comment
    
    #function checks for ul or ol element and adds p tags where applicable
    def listCheck(article):
        if re.search(r"<ul>[\s\S]*?</ul>", article):
            print(title + " has UL")
            article = re.split(r'(<ul>[\s\S]*?</ul>)', article)
            sub = '<ul>'
            for i, item in enumerate(article):
                if (sub in item):
                    pass
                else:
                    x = '<p>' + item + '</p>'
                    article[i] = x
        elif (re.search(r"<ol>[\s\S]*?</ol>", article)):
            print(title + "has OL")
            article = re.split(r'(<ol>[\s\S]*?</ol>)', article)
            sub = '<ol>'
            for i, item in enumerate(article):
                if (sub in item):
                    pass
                else:
                    x = '<p>' + item + '</p>'
                    article[i] = x
        article = (''.join(article))
        #print(article)
        return article
    
    article = listCheck(article)
    
    filename = str(title) + '.html'
    
    wrapper = f"""
        <head>
           <title>{title}</title>
       </head>
        <body>
            {article}
       </body>
    """
    
    f = open(filename, 'w')
    
    
    f.write(wrapper)
    f.close