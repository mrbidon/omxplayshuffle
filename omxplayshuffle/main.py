# -*- coding: utf8

import subprocess
import random
import logging
import os

debug = False

def run_bash(cmd_, cwd=".", out_err=False):
    if debug :
        print(cmd_)
        return "", ""
    else:
        p = subprocess.Popen(cmd_, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if stderr != "":
            print(stderr)
        if out_err:
            return stdout, stderr
        else:
            return stdout, ""

def remove_extension(path):
    a = path.split('.')
    return ".".join(a[:-1])


#return the list of file in a specified path
def get_files_list(path):
    files = list(os.walk(path))
    return files[0][2]

def main():
    while 1 :
        files = get_files_list(os.getcwd())
        random.shuffle(files)
        for file in files:
            file_without_ext = remove_extension(file)
            if not os.path.exists(file_without_ext+".lu"):
                run_bash("touch {0}".format(file_without_ext+".lu"))
                out, err = run_bash('omxplayer -b "{0}"'.format(file))
                print(out)
                print(err)
                
        run_bash("rm *.lu")

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                        level=logging.DEBUG)
    main()
