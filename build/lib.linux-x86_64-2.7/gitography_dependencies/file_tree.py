import os
import os.path


class BuildFileTree(object):

    def __filewalk(self):
        filetree = {}
        try:
            for path, _, files in os.walk(self.path):
                for f in files:
                    if f == 'Dockerfile':
                        filetree[os.path.basename(path)] = \
                            "%s/%s" % (path, f)
            if filetree:
                return filetree

        except IOError as e:
            print e

    def __init__(self, path):
        self.path = path
        self.filetree = self.__filewalk()
