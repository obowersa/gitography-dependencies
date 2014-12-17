import argparse

import dependencies


parser = argparse.ArgumentParser()


def setup_arguments():
    parser.add_argument("-r", "--repo", help="Location of the local\
                        local repo containing a Dockerfile")


def build(dict):
    for key, value in dict.iteritems():
        parent_key = ""
        parent_value = ""
        try:
            parent_key, parent_value = build(value[1])
        except:
            pass

        print "%s(%s) <- %s(%s)" % (key, value[0], parent_key, parent_value)
        return (key, value[0])


def main():
    setup_arguments()
    args = parser.parse_args()
    if args.repo:
        dependency = dependencies.DependencyTree(args.repo)
        dependency.build_tree()
        build(dependency.build_stack)
