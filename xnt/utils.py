from datetime import datetime


def str_to_datetime(date: str):
  return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

def list_to_datetime(list):
  return datetime(*list)

def list_to_timestamp(list):
  return datetime(*list).timestamp()

def tot_hits(response) -> int:
  return int(response['hits']['total']['value'])

# TODO : test
def summaries_from_response(response) -> list[dict]:
  return [a['summary'] for a in response['hits']['hits']]