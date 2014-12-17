import argparse

import dependencies


parser = argparse.ArgumentParser()


def setup_arguments():
    parser.add_argument("-r", "--repo", help="Location of the local\
                        local repo containing a Dockerfile")


def main():
    setup_arguments()
    args = parser.parse_args()
    print args.repo
