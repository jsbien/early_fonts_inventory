
The purposes of the phase 3 is to split a graphical character table
into the images of the individual glyphs and to provide an index to
the table in the djview4poliqarp format. We do not expect the results
to be perfect, this is just the first approximation.

This is the task of segment_character_table.py discussed below.

This is actually the continuation of the work done with ChatGPG
earlier, see in particular the chats
https://chatgpt.com/g/g-3s6SJ5V7S-askthecode-git-companion/c/1242785b-743b-49e0-9548-c0ae5d28d2a2,https://chatgpt.com/g/g-3s6SJ5V7S-askthecode-git-companion/c/97a64140-ee3e-48fd-b13a-6d1967b9c90c,
https://chatgpt.com/c/44a8833f-c231-4b23-aba0-35526e60d3fc,
https://chatgpt.com/c/1234fff2-fb30-4bcd-bcc2-87f371dd11c2,https://chatgpt.com/c/1b20d6cf-effa-4d73-a773-c39ac71a925b.

The starting point was the code of https://github.com/jpakkane/glyphtracer.

The script segment_character_table.py present in the repository
requires some adjustments.

1. We need two additional argument besides the first one which is the
input file. The second is: "DjVufile" explained later and used only as
string in the index creation process. The third is an optional one
"directory", defaulting to "tmp", for storing the results. 

2. The script creates an index. The updated specification of the index
is stored as index_format.md. The table identifier mentioned in the
specification is to be extracted from the input file name by removing
the "m" prefix. The Djvu document name is to be provided as the second
argument.

3. We need a log containing the number of recognized lines and the
number of letterboxes in every line. The file should be in plain text
format. The name of the log should be <input file base name>.log.  The
log should be both human and computer readable. The first line should
contains the arguments of the run. The subsequent lines can have the
form

<line number>: <number of letterboxes>

The last line should be a timestamp.

3. The second argument is used also to name the index file, the
extension "djvu" is to be replaced by "csv".

4. We don't need now to check whether the input file is binary,
because it was checked earlier. Hence the cheking code is to be
removed.

A typical call will be something like

python3 segment_character_table.py masks/m01.tiff Augezdecki-01a_PT08_403.djvu

The index line for this run should be similar to this

01 l 1 b 1;file:Augezdecki-01a_PT08_403.djvu.djvu?djvuopts=&page=1&highlight=47,903,63,104;Augezdecki-01a_PT08_403 l 1 b 1; ※
01 l 1 b 2;file:Augezdecki-01a_PT08_403.djvu.djvu?djvuopts=&page=1&highlight=136,903,70,104;Augezdecki-01a_PT08_403 l 1 b 2; ※
