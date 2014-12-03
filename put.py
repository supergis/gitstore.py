import argparse as ap
import os
import sys
import subprocess as sp
import json
import util

def put(args):
    proc = sp.Popen(['git', 'hash-object', '-w', '--stdin'], stdin=sp.PIPE, stdout=sp.PIPE)
    (sha0,_) = proc.communicate(args.data)
    sha = sha0.rstrip()
    updateIndexCmd = ['git', 'update-index', '--add', '--cacheinfo', '100644', sha, args.storefile]
    sp.call(updateIndexCmd)
    treeId = sp.check_output(['git', 'write-tree']).rstrip()
    commitCmd = ['git', 'commit-tree', treeId, '-m', 'blabla']
    if args.parent: # Use parent commit if the ref is valid
        refId = sp.check_output(['git', 'rev-parse', args.parent]).rstrip()
        if refId:
            commitCmd.append('-p')
            try:
                sp.check_call(['git', 'show-ref', args.parent], stdout=sp.PIPE)
                commitCmd.append('refs/heads/' + args.parent)
            except sp.CalledProcessError:
                commitCmd.append(refId)
    commitId = sp.check_output(commitCmd).rstrip()
    if args.ref:
        try:
            # Exception if ref does not exist
            sp.check_call(['git', 'show-ref', args.ref], stdout=sp.PIPE)
            if args.parent: # Try fast-forward from parent
                mergebase = sp.check_output(['git', 'merge-base', commitId, args.ref]).rstrip()
                refId = sp.check_output(['git', 'rev-parse', args.ref]).rstrip()
                if mergebase == refId:
                    sp.call(['git', 'update-ref', 'refs/heads/' + args.ref, commitId])
                    print json.dumps({'ref': args.ref})
                else:
                    print json.dumps({'ref': commitId})
            else:
                # Ref is taken and fast-forward is not possible
                print json.dumps({'ref': commitId})
        except sp.CalledProcessError:
            # Ref is unused, use it as new ref
            sp.call(['git', 'update-ref', 'refs/heads/' + args.ref, commitId])
            print json.dumps({'ref': args.ref})
    else:
        print json.dumps({'ref': commitId})

if __name__ == "__main__":
    parser = ap.ArgumentParser()

    parser.add_argument("storedir", help='directory of git repo')
    parser.add_argument("storefile", help='file in which data will be stored')
    parser.add_argument("data", help='the data to commit')
    parser.add_argument("--parent", help='specify parent commit')
    parser.add_argument("--ref", help='try as ref if possible, otherwise sha will be returned')

    args = parser.parse_args()

    if not util.gitDirExists(args.storedir):
        sys.exit(args.storedir + ' does not exist')

    os.chdir(args.storedir)
    put(args)
