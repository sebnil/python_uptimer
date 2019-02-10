# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import shelve
import time

from python_uptimer.defines import status_path


def start(resources, run_once=True):
    while True:
        d = shelve.open(status_path, writeback=True)

        result = {}
        for group in resources:
            result[group] = {}
            for job_name in resources[group]:
                r = resources[group][job_name].check()
                result[group][job_name] = r
        d['result'] = result
        d.sync()
        d.close()

        if run_once:
            break

        time.sleep(10)


def get_latest_status():
    d = shelve.open(status_path)
    return d['result']
