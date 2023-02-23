from flask import Flask, render_template
from urllib.request import urlopen
import feedparser
from datetime import datetime, timedelta

MAX_RESULT = 50 
SORTING = 'lastUpdatedDate'
CATEGORY = 'cs.AI'
PREFIX = 'cat'

app = Flask(__name__)

def is_recent(entry):
  yesterday = (datetime.today() - timedelta(days=2)).date()
  entry_date = datetime.strptime(entry.updated, "%Y-%m-%dT%H:%M:%SZ").date()
  return entry_date < yesterday 

def is_ai(entry):
  return entry.category == "cs.AI"

@app.route('/')
def get_news():
  base_url = 'http://export.arxiv.org/api/query?'
  # TODO : use a generator that returns once the articles is too old
  query = f"search_query={PREFIX}:{CATEGORY}&max_results={MAX_RESULT}&sortBy={SORTING}&sortOrder=descending&output=json" 
  response = urlopen(base_url + query).read() 
  feed = feedparser.parse(response)
  articles = [entry for entry in feed.entries if is_ai(entry)] 
  return render_template('news.html', title="News", articles = articles)
    

if __name__ == "__main__":
  app.run(port=5000, debug=True)
