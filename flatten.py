#!/usr/bin/python3
__author__ = 'otakucode'

import os, sys


def gather_lists(target):
    """Gathers 2 lists from target directory: list of subdirectories (and their subdirectories), and list of all files
       from the subdirectories recursively scanned."""
    # TODO: Filter out symlinks unless --follow-symlinks option is used.
    directory_list = []
    file_list = []
    for(path, dirs, files) in os.walk(target, topdown=False):
        directory_list.extend([os.path.join(path, d) for d in dirs])
        if path != target:      # Don't want to moves files already in the base directory
            file_list.extend([os.path.join(path, f) for f in files])

    return (directory_list, file_list)


def move_files(file_list, target):
    #print(file_list)
    dests = [os.path.join(target, os.path.basename(f)) for f in file_list]
    #print(dests)
    srcdests = zip(file_list, dests)
    #print(srcdests)
    # TODO: Add checking for proper permissions and for duplicate files
    try:
        for (src, dest) in srcdests:
            #print("Moving to %s" % dest)
            os.rename(src, dest)
    except OSError:
        print("ERROR: %s" % OSError.strerror)


def remove_dirs(dir_list):
    try:
        for dir in dir_list:
            os.rmdir(dir)
    except OSError:
        print("ERROR: %s" % OSError.strerror)


# TODO: Use argparse to process commandline arguments, add verbose mode to print files moved.
if len(sys.argv) != 2:
    print("Proper usage:")
    print("    flatten dir")
    print("Where 'dir' is the directory which you wish to be flattened.  All files contained in all subdirectories")
    print("of 'dir' will be recursively scanned and moved into 'dir'.  The subdirectories will then be removed.")
else:
    print("Scanning directories...")
    (directories, files) = gather_lists(sys.argv[1])
    print("Directories scanned: %s" % len(directories))
    print("Files found        : %s" % len(files))
    print("Moving files...")
    move_files(files, sys.argv[1])
    print("Removing directories...")
    remove_dirs(directories)
    print("Finished!")

