import os
import fnmatch

def locate(pattern, root=os.curdir):
    root_path = os.path.abspath(root)
    for path, dirs, files in os.walk(root_path):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)
