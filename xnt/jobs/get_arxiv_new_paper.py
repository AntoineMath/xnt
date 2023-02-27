from urllib.request import urlopen
from os import environ
import feedparser
from article import Article
from datetime import datetime, timedelta
from opensearchpy import OpenSearch
import json


MAX_RESULT = 50 
SORTING = 'lastUpdatedDate'
CATEGORY = 'cs.AI'
PREFIX = 'cat'

osearch_client = OpenSearch(
    hosts = [{'host': OSEARCH_HOST, 'port': OSEARCH_PORT}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = OSEARCH_AUTH,
    # client_cert = client_cert_path,
    # client_key = client_key_path,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
    ca_certs = CA_CERTS_PATH 
)


#TODO : write tests
def save_new_arxiv_articles():
  response = urlopen(f"http://arxiv.org/rss/{CATEGORY}").read()

  # get recent articles
  feed = feedparser.parse(response)
  articles = [json.dumps(entry) for entry in feed.entries] 
  
  # TODO: write in a file the last added articles instead of querying the db every minute

  # filter articles
  articles = [a for a in articles if not osearch_client.exists(INDEX, json.loads(a)['id'])]

  #with open("/Users/mathurin/fun/xnt/logs.txt", "a") as f:
  #  f.write(f"added {len(articles)} articles")

  # index new articles
  for article in articles:
    osearch_client.index(
      index = INDEX,
      body = article,
      id = json.loads(article)['id'],
      refresh = True
    )

if __name__ == "__main__" :
  save_new_arxiv_articles()
  
