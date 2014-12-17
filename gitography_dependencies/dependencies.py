#!/usr/bin/python

import sys
import clone
import file_tree
import parse_dockerfile


class DependencyTree(object):

    def __check_parsed(self, parsed_file):
        if parsed_file.repo == "":
            print >> sys.stderr, "%s missing repo" % (parsed_file)
            return False
        elif parsed_file.registry == "":
            print >> sys.stderr, "%s missing registry" % (parsed_file)
            return False
        return True

    def __parse_tree(self):
        parsed_files = {}
        try:
            for key, value in self.filetree.iteritems():
                parsed_file = parse_dockerfile.Dockerfile(value)
                if self.__check_parsed(parsed_file):
                    parsed_files[key] = parsed_file
                else:
                    print >> sys.stderr, "Unable to parse %s" \
                        % (parsed_files[key])
            return parsed_files
        except:
            print "Unable to access Dockerfile"


    def __init__(self, path):
        self.path = path
        filetree = file_tree.BuildFileTree(path)
        self.filetree = filetree.filetree
        self.parsed_files = self.__parse_tree()
        self.build_stack = {}

    def build_tree(self):
        for key in self.parsed_files:
            f = self.parsed_files[key]
            self.build_stack = {f.image: [f.dockerfile]}
            if f.built:
                return self.build_stack
            else:
                path = '/tmp/%s%s' % (f.image, f.tag)
                print >> sys.stderr, "Cloning %s" % (path)
                clone.GitClone(f.repo, path).clone()
                temp_deptree = DependencyTree(path)
                self.build_stack[f.image].append(temp_deptree.build_tree())
                return self.build_stack
