DDJVU --- DjVuLibre-3.5.28
DjVu decompression utility

Usage: ddjvu [options] [<djvufile> [<outputfile>]]

Options:
  -verbose          Print various informational messages.
  -format=FMT       Select output format: pbm,pgm,ppm,pnm,rle,tiff.
  -scale=N          Select display scale.
  -size=WxH         Select size of rendered image.
  -subsample=N      Select direct subsampling factor.
  -aspect=no        Authorize aspect ratio changes
  -segment=WxH+X+Y  Select which segment of the rendered image
  -mode=black       Render a meaningful bitonal image.
  -mode=mask        Only render the mask layer.
  -mode=foreground  Only render the foreground layer.
  -mode=background  Only render the background layer.
  -page=PAGESPEC    Select page(s) to be decoded.
  -skip             Skip corrupted pages instead of aborting.
  -eachpage         Produce one file per page (using %d in outputfile).
  -quality=QUALITY  Specify jpeg quality for lossy tiff output.

If <outputfile> is a single dash or omitted, the decompressed image
is sent to the standard output.  If <djvufile> is a single dash or
omitted, the djvu file is read from the standard input.
