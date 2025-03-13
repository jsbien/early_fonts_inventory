Please write the script named `masks.py' which will perform the task
described below.

Iterate over the lines in names.csv files in the root directory.

The second field contains the name of the file to be processed, the
files are in the DjVu directory.

The first field <numer> is used to created the name of the output
file, namely m<number>.tiff, the output files are to be placed in the
`masks' directory.

The processing consists in extracting so called mask from a DjVu
files. It is to be done by calling `dddjvu` with the parameters
`-mode=mask -format=tiff`. You can consult the program man page, for
convenience the help output is placed in the repository as ddjvu.md.
There is also a discussion at https://sourceforge.net/p/djvu/bugs/357/
caused by incorrect format recognition by a python script (the problem
seems to persist, but it belongs to the next phase).

To be on the safe side, the program should check the output is binary
as it should be. You can use for it the code from
`segment_character_table.py` in this repository, namely
is_black_and_white and/or detect_black_index.

If possible, please commit the script to the repository.
