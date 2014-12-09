import argparse as ap
import os
import sys
import subprocess as sp
import json
import util

def listBranch():
    branches = sp.check_output(['git', 'branch']).split('\n')
    branches.pop()
    print json.dumps(map(lambda x: x.strip(), branches))

if __name__ == "__main__":
    parser = ap.ArgumentParser()

    parser.add_argument("storedir", help='directory of git repo')
    parser.add_argument("--list", help='get all commits in that ref')

    args = parser.parse_args()

    if not util.gitDirExists(args.storedir):
        sys.exit(args.storedir + ' does not exist')

    os.chdir(args.storedir)
    if args.list == 'branch':
        listBranch()
