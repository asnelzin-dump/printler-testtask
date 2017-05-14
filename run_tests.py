# coding=utf-8

"""
Не уверен, самый ли это удачный вариант запуска тестов.
Скорее всего, unittest'ы были бы лучшим решением, но я выбрал этот способ,
в связи с данной формулировкой задачи.

python run_tests.py operations.py
python run_tests.py allocation.py
"""
import os
import sys
import subprocess


def group(lst, n):
    """group([0,3,4,10,2,3], 2) => [(0,3), (4,10), (2,3)]
    Group a list into consecutive n-tuples. Incomplete tuples are
    discarded e.g.

    >>> group(range(10), 3)
    [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    """
    return zip(*[lst[i::n] for i in range(n)])


def main():
    executable = sys.argv[1]
    file_name = os.path.splitext(executable)[0]
    tests_folder = 'tests/%s' % file_name
    test_cases = group(os.listdir(tests_folder), 2)

    for test_case in test_cases:
        with open(os.path.join(tests_folder, test_case[0])) as test_case_input, \
                open(os.path.join(tests_folder, test_case[1])) as test_case_output:
            proc = subprocess.Popen(['python', executable], stdin=test_case_input, stdout=subprocess.PIPE)
            out, err = proc.communicate()
            right_output = test_case_output.read().strip()
            if out.strip() == right_output:
                print 'OK'
            else:
                print 'FAIL'


if __name__ == '__main__':
    main()