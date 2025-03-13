The directory DjVu contains the file with the base names in the form:
<printer>-<font>_PT<fascicule>_<plate>

<printer> is an alphabetic string sometimes with non-ASCII letters
<font> starts with a two digit number which can have various postfixes
<fascicule> is a two digit number
<plate> is a tree digit number

Please write a script named `names.py' which will parse the names and
place the results in the CSV file named names.csv, which is present in
the root directory and in the beginning contains only the
header.

After sorting fill the `number' field with the subsequent 2 digit
numbers starting with 1.

Please insert also as field 2 the complete with name (with the
extension).

So the header will be:
number,file_name,printer,font,fascicule,plate


If possible please commit the script to the repository.
