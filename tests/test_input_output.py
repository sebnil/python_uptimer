# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import unittest
from python_uptimer import up_check
from python_uptimer import monitor_runner
from python_uptimer.defines import status_path
import shelve


class MyTestCase(unittest.TestCase):

    resources = {
        'sebastiannilsson.com': {
            'web': up_check.Response('http://sebastiannilsson.com')
        },
        'python': {
            'web': up_check.Response('http://python.org'),
            'docs': up_check.Response('http://docs.python.org'),
        },
        'faultcase': {
            'hi404': up_check.Response('http://this-website-does-not-exist-so-hi-404.se'),
        }
    }

    def test_input(self):
        monitor_runner.start(self.resources, run_once=True)
        d = shelve.open(status_path)
        self.assertTrue(d['result']['sebastiannilsson.com']['web']['success'])
        self.assertTrue(d['result']['python']['docs']['success'])
        self.assertTrue(d['result']['python']['web']['success'])
        self.assertFalse(d['result']['faultcase']['hi404']['success'])


    def test_output(self):
        self.test_input()
        o = monitor_runner.get_latest_status()
        self.assertGreater(len(o), 0)


    def test_shelve(self):
        shelf = shelve.open("myshelf.db", writeback=True)
        shelf['thedict'] = {'one': 1, 'two': 2, 'three': 3}
        shelf.sync()
        shelf.close()

if __name__ == '__main__':
    unittest.main()
