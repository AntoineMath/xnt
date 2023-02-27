import json

class Article():
    def __init__(self, feed_entry=None):
        if feed_entry:
            self.title = feed_entry.title 
            self.summary = feed_entry.summary
            self.link = feed_entry.link 
            #self.updated = feed_entry.updated


    def to_json(self):
        return json.loads(json.dumps(self.__dict__))