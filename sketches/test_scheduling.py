# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import unittest
import schedule
import time


class MyTestCase(unittest.TestCase):
    def test_schedule(self):
        def job():
            print(time.time())

        schedule.every(2).seconds.do(job)
        while True:
            schedule.run_pending()
            # time.sleep(1)
            break


if __name__ == '__main__':
    unittest.main()
