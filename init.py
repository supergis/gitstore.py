import argparse as ap
import os
import sys
import subprocess as sp
import util

def init(args):
    os.mkdir(args.storedir)
    os.chdir(args.storedir)
    sp.call(['git', 'init', '--bare'])

if __name__ == "__main__":

    parser = ap.ArgumentParser()

    parser.add_argument("storedir", help='directory of git repo')

    args = parser.parse_args()

    if util.gitDirExists(args.storedir):
        sys.exit(args.storedir + " already exists")

    init(args)
