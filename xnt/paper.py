import json
from datetime import datetime

class Paper():
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.updated_parsed = data['updated_parsed']
        self.summary = data['summary']
        self.category = data['arxiv_primary_category']['term']
        self.link = data['link']
        self.update_timestamp = datetime(*data['updated_parsed'][:6]).timestamp()
        self.update_datetime = datetime(*data['updated_parsed'][:6])
 

    @property
    def updated_datetime(self): return datetime(*self.updated_parsed[:6])


    def to_json(self):
        return json.loads(json.dumps(self.__dict__))