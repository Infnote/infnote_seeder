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
    sys.argv[1] is a full node IP
    sys.argv[2] is the seed url
    sys.argv[3] is sleep seconds
    '''
    if len(sys.argv) == 2:
        re_exe('python3 crawler.py ' + sys.argv[1], 60)
    elif len(sys.argv) == 3:
        re_exe('python3 crawler.py ' + sys.argv[1] + ' ' + sys.argv[2], 60)
    elif len(sys.argv) == 4:
        re_exe('python3 crawler.py ' + sys.argv[1] + ' ' + sys.argv[2] , int(sys.argv[3]))
    else:
        re_exe('python3 crawler.py', 60)
