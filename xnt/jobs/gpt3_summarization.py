import openai


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

if __name__ == "__main__":
  summarize("text")