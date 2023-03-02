import json
import openai
from xnt import app, osearch
from xnt.gpt3_completion import GPT3_response

INDEX = app.config['INDEX']
SIZE = 30 # TODO: be smarter
SUM_FIELD = "abstract-summary"
GPT3_MODEL = "text-davinci-003"

# TODO: batch process the unsummarized papers
def summarize(text: str, model: str) -> str:
  instructions = "sumup the following text in 1 concise sentence: " + text

  completion = openai.Completion.create(
    model=model, # for test purposes, cheaper
    prompt=instructions,
    temperature=0, # deterministic answer (good for scientific summarization) 
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.3,
    presence_penalty=1,
    stream = False,
  ) 
  return completion


def get_papers_wo_summary() -> list[dict]:
  query = {
    "query": {
      "bool": {
        "must_not": [
          {
            "nested": {
              "path": "abstract-summary",
              "query": {
                "exists": {
                  "field": "abstract-summary"
                }
              }
            }
          }
        ]
      }
    }
  }
  return [p for p in osearch.search(index=INDEX, body=query, size = SIZE)['hits']['hits']] 

def add_sum_to_paper(index, paper_id: str, summary: str, cost: dict) -> None:
  query = {
    "doc": {
      "abstract-summary" : {
        "text": summary,
        "cost": cost
     }
    }
  }
  osearch.update(index=index, id=paper_id, body=query)



if __name__ == "__main__":
  papers_to_sumup = get_papers_wo_summary()
  for p in papers_to_sumup:
    abstract = p['_source']['summary']
    gpt3_response = GPT3_response(summarize(abstract, GPT3_MODEL))
    add_sum_to_paper(INDEX, p["_id"], gpt3_response.text, gpt3_response.cost_details)
    print(abstract + "\n\n")
    print(gpt3_response.text)
    print("****************")