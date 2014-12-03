import os
import subprocess as sp

def gitDirExists(d):
    isGitRepo = not sp.call(['git', 'rev-parse', '--is-inside-work-tree'], stdout=sp.PIPE)
    if os.path.isdir(d):
        os.chdir(d)
        return isGitRepo
    else:
        return False
