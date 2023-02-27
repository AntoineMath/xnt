import os 
import json 
import openai 
from flask import render_template 
from urllib.request import urlopen
import feedparser
from datetime import datetime, timedelta
from xnt import app, osearch 
from xnt.article import Article

INDEX = app.config['DEV_INDEX']
GPT3_ACTIVATED = False
SORTING = 'lastUpdatedDate'
CATEGORY = 'cs.AI'
PREFIX = 'cat'


def is_recent(entry):
  yesterday = (datetime.today() - timedelta(days=2)).date()
  entry_date = datetime.strptime(entry.updated, "%Y-%m-%dT%H:%M:%SZ").date()
  return entry_date < yesterday 

def is_ai(entry):
  return entry.category == "cs.AI"

@app.route('/')
def news():
  # TODO : search with date and display GPT3 summarization
  articles = [a['_source'] for a in osearch.search(index=INDEX)['hits']['hits']]
  return render_template('news.html', title="News", articles = articles)
    

