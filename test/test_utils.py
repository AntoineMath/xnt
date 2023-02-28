import unittest
from xnt.utils import str_to_datetime, list_to_datetime, list_to_timestamp, tot_hits


class TestUtils(unittest.TestCase):
    def test_str_to_datetime(self):
      old_date = '2023-02-27T18:59:55'
      new_date = '2023-02-27T18:59:56'

      assert str_to_datetime(old_date) < str_to_datetime(new_date)

    def test_list_to_datetime(self):
      old_date = [2023, 2, 27, 18, 59, 55]
      new_date = [2023, 2, 27, 18, 59, 56]

      assert list_to_datetime(old_date) < list_to_datetime(new_date)

    def test_list_to_timestamp(self):
      old_date = [2023, 2, 27, 18, 59, 55]
      new_date = [2023, 2, 27, 18, 59, 56]
      assert list_to_timestamp(old_date) < list_to_timestamp(new_date)

    def test_tot_hits(self):
      no_result_response = {'took': 2, 'timed_out': False, '_shards': {'total': 1, 'successful': 1, 'skipped': 0, 'failed': 0}, 'hits': {'total': {'value': 0, 'relation': 'eq'}, 'max_score': None, 'hits': []}}

      assert tot_hits(no_result_response)  == 0



if __name__ == "__main__":
   unittest.main()