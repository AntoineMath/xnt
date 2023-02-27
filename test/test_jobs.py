import unittest
from urllib.request import urlopen
import feedparser
import json
#from xnt.article import Article

class TestJobs(unittest.TestCase):
    def test_get_arxiv_new_paper(self):
        CATEGORY = 'cs.AI'
        response = urlopen(f"http://arxiv.org/rss/{CATEGORY}").read()
        feed = feedparser.parse(response)
        print(json.dumps(feed.entries[0], indent=2))
        #articles = [Article(entry) for entry in feed.entries] 


if __name__ == "__main__":
    unittest.main()