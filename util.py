import os
import subprocess as sp

def gitDirExists(path):
    isGitRepo = not sp.call(['git', 'rev-parse', '--is-inside-work-tree'], stdout=sp.PIPE)
    if os.path.isdir(path):
        os.chdir(path)
        return isGitRepo
    else:
        return False
