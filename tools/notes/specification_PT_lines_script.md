The name of the script is PT_lines.py.  It takes an obligatory
argument: the path to the direcory containing the files to be
processed.

The directory contains about 100 files  The files are binary in the
PNG format. 

For every file a subdirectory is created named with the basename
postfixed with "_lines".

Than the file is split into lines, every line is stored in the
appropriate subdirectory in a separate file named with the basename
prefixed by two digit line numer.

A log should be created named PT_lines_<time_stamp>.py contaning the
script version. the coordinates of the recognized lines and the number
of lines. The intention is to check the logs for possible regression
bugs.
