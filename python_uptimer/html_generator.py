# force python 3.* compability
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
# regular imports below:
from yattag import Doc
from python_uptimer import monitor_runner


def generate_html(file_name='result.html'):
    results = monitor_runner.get_latest_status()
    print(results)

    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('body'):
            with tag('table', style='width: 100%'):
                for group in sorted(results):
                    with tag('tr'):
                        with tag('td', klass='group', colspan='3'):
                            with tag('h3', style='margin: 10px 0 0 0;'):
                                text(group)
                    for job_name in results[group]:
                        with tag('tr') as tr:
                            r = results[group][job_name]
                            if r['success']:
                                doc.attr(style='background: green;')
                            else:
                                doc.attr(style='background: red;')
                            with tag('td'):
                                text(job_name)
                            with tag('td'):
                                text(r['success'])
                            with tag('td'):
                                try:
                                    text('{:.1f}s'.format(r['response_time'].total_seconds()))
                                except:
                                    text('')
                            print(r)

    html = doc.getvalue()
    print(html)
    with open(file_name, "w", encoding='utf-8-sig') as f:
        f.write(html)


if __name__ == '__main__':
    generate_html()
