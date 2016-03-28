# -*- coding: utf8

import subprocess
import random
import logging
import os

def run_bash(cmd_, cwd=".", out_err=False):
    p = subprocess.Popen(cmd_, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stderr != "":
        print stderr
    if out_err:
        return stdout, stderr
    else:
        return stdout, ""

#return the list of file in a specified path
def get_files_list(path):
    files = []
    for file in next(os.walk(path))[2]:
        files.append(file)
    logging.debug(files)
    return files

def main():
    print os.getcwd()
    files = get_files_list(os.getcwd())
    random.shuffle(files)
    for file in files:
        out, err = run_bash("omxmplayer {0}".format(file))
        print out
        print err


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                        level=logging.DEBUG)
    main()
