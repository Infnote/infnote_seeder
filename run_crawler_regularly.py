import time
import os
import sys


def re_exe(cmd, inc=300):
    '''
    :param cmd:
    :param inc: 300 seconds
    :return:
    '''
    while True:
        os.system(cmd)
        time.sleep(inc)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        re_exe('python3 crawler.py ' + sys.argv[1], 300)
    else:
        re_exe('python3 crawler.py', 300)
