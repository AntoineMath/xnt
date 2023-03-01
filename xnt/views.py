from flask import render_template , request
from datetime import datetime, timedelta
from xnt import app, osearch 

INDEX = app.config['INDEX']
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
  time=request.args.get("time")
  papers = [p['_source'] for p in osearch.search(index=INDEX)['hits']['hits']]
  return render_template('news.html',
                         title="News",
                         papers = papers,
                         time=time)
    