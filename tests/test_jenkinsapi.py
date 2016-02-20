# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import unittest
from jenkinsapi.jenkins import Jenkins
from python_uptimer.jenkins_check import JenkinsNodeAlive
from python_uptimer import monitor_runner


class MyTestCase(unittest.TestCase):
    def test_slave_alive(self):
        J = Jenkins('http://builds.apache.org/',)
        test_slave = J.get_node('H0')
        test_slave.is_online()


    def test_jenkins_check(self):
        resources = {
            'builds.apache.org': {
                'master': JenkinsNodeAlive('http://builds.apache.org/', node_name='master'),
                'H0': JenkinsNodeAlive('http://builds.apache.org/', node_name='H0'),
            }
        }
        monitor_runner.start(resources, run_once=True)
        d = monitor_runner.get_latest_status()
        self.assertTrue(d['builds.apache.org']['master']['success'])
        self.assertTrue(d['builds.apache.org']['H0']['success'])

if __name__ == '__main__':
    unittest.main()
