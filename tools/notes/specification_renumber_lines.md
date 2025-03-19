Specification of `renumber_lines.py` for ChatGPG

Two arguments: input and output directories

The input direcory contains the files named according to the schema

m<number1>_R_lines_<numer2><optional subnumber2>.png

The file should renumber in such a way that their alphabetical order
is preserved, subnumbers are eliminated and both number1 and number2
are continuous (starting with 01).

So the names

m19_R_lines_02.png
m19_R_lines_03-1.png
m19_R_lines_03-2.png

should be changed to

m19_R_lines_02.png
m19_R_lines_03.png
m19_R_lines_04.png

Moreover a statistic should be printed, which shows
- for every number1 the maximal value of number2
- the total number of files.
