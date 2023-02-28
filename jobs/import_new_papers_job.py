import json
import feedparser
from urllib.request import urlopen
from opensearchpy.helpers import bulk
from xnt import app, osearch
from xnt.paper import Paper 
from xnt.utils import str_to_datetime

# TODO : write tests
# TODO : make it async 
# TODO: write in a file the last added papers instead of querying the db every minute

INDEX = app.config['INDEX']
CATEGORIES = ['cs.AI']
BS = 10
MAX_QUERIES = 5 # for safety (we look at the 10x5 last papers in cs category)

def import_new_arxiv_papers():

  papers_to_save = []

  if osearch.count(index=INDEX, body={"query": {"match_all":{}}})['count'] > 0:
    last_updated_paper = osearch.search(index=INDEX,
                                        body = {"query": {"match_all":{}}},
                                        size=1,
                                        sort="update_datetime:desc") 
    last_updated_date = str_to_datetime(last_updated_paper['hits']['hits'][0]['_source']['update_datetime'])
  else: 
    last_updated_date = None


  # find more recent papers
  for i in range(MAX_QUERIES): 
    response = urlopen(f"http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=lastUpdatedDate&sortOrder=descending&max_results={BS}&start={i*BS}").read()
    feed = feedparser.parse(response)
    papers = [Paper(json.loads(json.dumps(entry))) for entry in feed.entries] 
    for p in papers:
      if last_updated_date is not None and p.updated_datetime >= last_updated_date:
        break
      if p.category in CATEGORIES:
        papers_to_save.append(
          {"_index": INDEX,
           "_id": p.id,
           "_source": p.__dict__
          })
    else: continue 
    break
         

  # bulk index new papers
  bulk(osearch, papers_to_save)

  # log
  with open("logs.txt", "a") as f:
    f.write(f"added {len(papers_to_save)} papers")

  for p in papers_to_save:
    print(f"saved : {p['_source']['title']}\n")

if __name__ == "__main__" :
  import_new_arxiv_papers()
