import json
from urllib.request import urlopen
import feedparser
from xnt import app, osearch
from xnt.utils import is_cat

INDEX = app.config['INDEX']
CATEGORY = 'cs.AI'

#TODO : write tests
def save_new_arxiv_articles():
  response = urlopen(f"http://arxiv.org/rss/{CATEGORY}").read()

  # get recent articles
  feed = feedparser.parse(response)
  articles = [json.dumps(entry) for entry in feed.entries] 
  
  # TODO: write in a file the last added articles instead of querying the db every minute

  # filter articles
  articles = [a for a in articles if f"[{CATEGORY}]" in json.loads(a)['title'] and not osearch.exists(INDEX, json.loads(a)['id'])]

  # index new articles
  for article in articles:
    osearch.index(
      index = INDEX,
      body = article,
      id = json.loads(article)['id'],
      refresh = True
    )

  # log
  with open("logs.txt", "a") as f:
    f.write(f"added {len(articles)} articles")

if __name__ == "__main__" :
  save_new_arxiv_articles()
  
