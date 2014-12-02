import argparse as ap
import os
import sys
import subprocess as sp
import json

parser = ap.ArgumentParser()

parser.add_argument("storedir", help='directory of git repo')
parser.add_argument("storefile", help='file in which data will be stored')

parser.add_argument("--ref", help='ref to commit')
parser.add_argument("--tree", help='get all commits in that ref')

args = parser.parse_args()

if __name__ == "__main__":
    os.chdir(args.storedir)
    if args.tree:
        revList = sp.check_output(['git', 'rev-list', args.tree]).split('\n')
        revList.pop()
        def show(sha):
            d = sp.check_output(['git', 'show', sha + ':' + args.storefile])
            return d
        data = map(show, revList)
        print json.dumps(data)
    elif args.ref:
        commitId = sp.check_output(['git', 'rev-parse', args.ref]).rstrip()
        d = sp.check_output(['git', 'show', commitId + ':' + args.storefile])
        print json.dumps(d)
