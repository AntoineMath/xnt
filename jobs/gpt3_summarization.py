import aiohttp
import openai
import xnt
from xnt import app, osearch
INDEX = app.config['INDEX']
SIZE = 30 # TODO: be smarter


# TODO: batch process the unsummarized papers
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

async def summarize():
  async with aiohttp.ClientSession() as session:
    openai_api_url = ''

def get_papers_wo_summary():
  query = {
    "query": {
      "bool": {
        "must_not": {
          "exists": {
            "field": "gpt3-summary"
          }
        }
      }
    }
  }
  osearch.search(index=INDEX, body=query, size = SIZE) 


if __name__ == "__main__":
