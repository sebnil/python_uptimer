# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
from jenkinsapi.jenkins import Jenkins


class JenkinsNodeAlive():
    def __init__(self, jenkins_url, username=None, password=None, node_name='master'):
        self.jenkins_url = jenkins_url
        self.node_name = node_name
        self.username = username
        self.password = password

    def check(self):
        r = {}
        try:
            J = Jenkins(self.jenkins_url, username=self.username, password=self.password)
            test_slave = J.get_node(self.node_name)
            r['name'] = self.node_name
            r['success'] = test_slave.is_online()
        except:
            print('Something went wrong checking {}'.format(self.jenkins_url))
            r['success'] = False
        return r
