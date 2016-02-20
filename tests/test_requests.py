# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import unittest
from python_uptimer import up_check
import requests

class MyTestCase(unittest.TestCase):



    def test_response_time(self):
        jobs = [
            up_check.Response('http://sebastiannilsson.com'),
            up_check.Response('http://treplex.se'),
            up_check.Response('http://google.com'),
        ]
        for job in jobs:
            r = job.check()
            print(r)


    def test_requests(self):
        response = requests.get('http://www.google.com', timeout=2)
        self.assertGreater(len(response.content), 0)
        self.assertGreater(response.elapsed, -1)


if __name__ == '__main__':
    unittest.main()
