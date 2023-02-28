import aiohttp
import openai
import xnt
from xnt import app, osearch
INDEX = app.config['INDEX']


# TODO: batch process the unsummarized articles
def summarize(text):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.7,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=1
  ) 
  return response

async def main():
  async with aiohttp.ClientSession() as session:
    openai_api_url = ''
def get_papers_wo_summary():
  query = {
    'query': {
      'bool': {
        'must_not': {
          'exists': {
            'field': 'gpt3-summary'
          }
        }
      }
    }
  }
  return osearch.search(index=INDEX, body=query) 


if __name__ == "__main__":
  for p in get_papers_wo_summary()['hits']['hits']:
    print(p['_source']['title'], '\n')
  summarize("text")