import time
import os
import sys


def re_exe(cmd, inc=60):
    '''
    :param cmd:
    :param inc: 60 seconds
    :return:
    '''
    while True:
        os.system(cmd)
        time.sleep(inc)


if __name__ == "__main__":
    '''
    sys.argv[1] is IP
    sys.argv[2] is sleep seconds
    '''
    if len(sys.argv) == 2:
        re_exe('python3 crawler.py ' + sys.argv[1], 60)
    elif len(sys.argv) == 3:
        re_exe('python3 crawler.py ' + sys.argv[1], int(sys.argv[2]))
    else:
        re_exe('python3 crawler.py', 60)
