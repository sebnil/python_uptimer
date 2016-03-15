# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import unittest
from python_uptimer import up_check
from python_uptimer import monitor_runner
from python_uptimer.defines import status_path
from python_uptimer.junit_xml_generator import generate_junit_xml
import python_uptimer

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

class MyTestCase(unittest.TestCase):



    def test_xml_generation(self):
        monitor_runner.start(resources, run_once=True)
        generate_junit_xml('junit.xml')
