import os
import subprocess as sp

def gitDirExists(path):
    return os.path.isdir(path)
