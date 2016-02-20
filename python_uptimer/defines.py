# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
import os
import errno


# path to this script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

csv_directory = dname + '/csv/'
make_sure_path_exists(csv_directory)

shelves_directory = dname
status_path = shelves_directory + '/status'
