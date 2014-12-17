#!/usr/bin/python

import argparse
import os
import subprocess


def parse_arguments():

    parser = argparse.ArgumentParser(description='Wrapper for condor')
    parser.add_argument('-i', '--input_dir',
                        help='Location of files to be submitted',
                        required='True')
    parser.add_argument('-b', '--branch',
                        help='Name of branch', required='False')
    args = parser.parse_args()

    return (args.input_dir, args.branch)


def check_filestructure(file_structure):
    for key, value in file_structure.iteritems():
        if not os.path.exists(value):
            return False

    return True


def main():

    input_dir, branch = parse_arguments()
    if os.path.exists(input_dir):
        file_structure = {'build': input_dir,
                          'source': input_dir + 'src',
                          'environment': input_dir + 'env'}

        if check_filestructure(file_structure):
            os.chdir(input_dir)
            subprocess.call("condor_submit submit.condor", shell=True)
        else:
            print "Not a valid file structure"
    else:
        print "Could not locate directory"


if __name__ == '__main__':
    main()
