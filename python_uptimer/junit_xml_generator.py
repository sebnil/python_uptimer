# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
from junit_xml import TestSuite, TestCase
from python_uptimer import monitor_runner

def generate_junit_xml(file_name='junit.xml'):
    results = monitor_runner.get_latest_status()
    print(results)

    test_suites = []

    #test_cases = [TestCase('Test1', 'some.class.name', 123.345, 'I am stdout!', 'I am stderr!')]
    #ts = TestSuite("my test suite", test_cases)
    for testsuite_name in results:
        test_cases = []
        for test_case_name in results[testsuite_name]:
            name = results[testsuite_name][test_case_name]['name']
            success = results[testsuite_name][test_case_name]['success']

            try:
                elapsed_sec=results[testsuite_name][test_case_name]['response_time'].total_seconds()
            except:
                elapsed_sec=-1
            tc = TestCase(
                name=name,
                classname='{}.{}'.format(testsuite_name, test_case_name),
                elapsed_sec=elapsed_sec,
                stdout='{}'.format(success),
            )
            if success is False:
                tc.add_failure_info('Failed')
            test_cases.append(tc)
        ts = TestSuite(testsuite_name, test_cases)
        test_suites.append(ts)
    pass

    with open(file_name, "w", encoding='utf-8-sig') as f:
        TestSuite.to_file(f, test_suites, prettyprint=True)