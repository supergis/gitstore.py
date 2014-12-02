import argparse as ap
import os
import sys
import subprocess as sp

parser = ap.ArgumentParser()

parser.add_argument("storedir", help='directory of git repo')

args = parser.parse_args()

if __name__ == "__main__":
    if not os.path.isdir(args.storedir):
        os.mkdir(args.storedir)
        os.chdir(args.storedir)
        sp.call(['git', 'init', '--bare'])
    else:
        sys.exit(directory + " already exists")
