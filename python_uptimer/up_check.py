# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import requests
import time
import string

from python_uptimer.defines import csv_directory

class Response():

    def __init__(self, url, filename=None):
        if not url.startswith('http://'):
            self.url = 'http://{}'.format(url)
        else:
            self.url = url

        if filename != None:
            self.filename = filename
        else:
            self.filename = slugify(self.url)


    def check(self):
        try:
            unixtime = time.time()
            response = requests.get(self.url, timeout=10)

            print('getting {} took {}'.format(self.url, response.elapsed))
            r = {
                'name': self.url,
                'time': unixtime,
                'success': True,
                'response_time': response.elapsed,
            }
        except:
            print('getting {} failed'.format(self.url))
            r = {
                'name': self.url,
                'time': unixtime,
                'success': False,
                'response_time': None,
            }
        self.log_result(r)
        return r

    def log_result(self, r):
        with open('{}/{}.csv'.format(csv_directory, self.filename), 'a+', encoding="utf-8") as f:
            line = '{time},{success},{response_time}\n'.format(time=r['time'], success=r['success'], response_time=r['response_time'])
            f.write(str(line))


def slugify(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in filename if c in valid_chars)