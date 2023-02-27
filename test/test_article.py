import unittest
from xnt.article import Article

class TestArticle(unittest.TestCase):

  def test_to_json(self):
    article = Article()
    article.title = "test_title"
    article.summary = "test_summary"
    article.link = "test_link"
    article.updated = "test_updated"
    json = article.to_json()

    assert json["title"] == "test_title"
    assert json["summary"] == "test_summary"
    assert json["link"] == "test_link"
    assert json["updated"] == "test_updated"


if __name__ == "__main__":
  unittest.main()





