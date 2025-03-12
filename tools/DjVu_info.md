# djvu2mask
Extracting binary mask from DjVu documents on Debian Linux

A Python script:

For every *.djvu file in the specified directory do the following

1. Extract the mask with

`ddjvu -verbose -format=tiff -mode=mask <file name>.djvu <file name>_mask.tiff`

2. Print ouput properties with identify
https://sourceforge.net/p/djvu/bugs/357/


Ad 1

ddjvu -1 should always return a binary mask as a PBM files.
PBM files can only represent binary images anyway.
https://linux.die.net/man/5/pbm

https://sourceforge.net/p/djvu/bugs/357/

Option -1 or --subsample=1 ensure that the output resolution matches 
that of the input image.
Note that this is the default when you use the --format option (which 
you should always use.)

Note that when you use --format=pbm, you force the output to be a pbm 
file which can only encode binary images.
Even if you were to subsample the image (making the mask gray level), it 
would be tresholded into a binary image to produce a pbm file.
These PBM files start with the two letters "P4". If this is the case, 
this is a binary image and nothing else. If the png is not binary, then 
this must come from the downstream conversion. Note that you can also 
use "--verbose" to let ddjvu tell you.

If you do not like these pbm/pgm/ppm files, you might like --format=tiff 
which is usually smart enough to decide a binary, grey level, or color 
encoding. You can then use program tiff info to know what you got. It 
automatically use lossless CCITT-T4 compression for binary images. For 
other images, it uses packbits (the most portable lossless scheme) by 
default, jpeg compression with option "--quality=<1to100>", and 
additionally understands "--quality=deflate|lzw|raw". People usually 
say that this works nicely for them. Then you might use a program like 
tiff2png which I believe keeps the tiff setup into the png (as much as 
png allows). Best would be to use the tiff files directly though 
(they're more flexible).


