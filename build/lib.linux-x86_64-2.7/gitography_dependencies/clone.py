import subprocess
import os


class GitClone(object):
    E_INVALID_DST = 129

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def clone(self):
        if not os.path.isdir(self.dst):
            clone = subprocess.Popen(
                ['/usr/bin/git', 'clone', self.src, self.dst])
            return clone.wait()
        else:
            return GitClone.E_INVALID_DST
