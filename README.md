# flatten

A simple utility to flatten directory trees.  Run with Python 3 specifying the target directory as a commandline argument.  All files contained in subdirectories under that directory will be moved to that specified directory and all subdirectories will be recursively deleted.  This program is not even in alpha status.  It is not complete.  It does not even check for duplicate files being moved and can result in data loss if used carelessly.  It will soon be updated to handle duplicate files and file permissions issues.  I strongly recommend that you search the web for a shell script or other equivalent utility rather than using this program in its current state.


NOTE: This software was written quickly for personal use and currently lacks comprehensive error checking, unit tests, and other niceities which software written for public distribution should include. Please review the code before running.
