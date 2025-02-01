for file in *.png; do
    convert "$file" +profile "*" -deskew 10% -type Bilevel -debug Transform "${file%.png}_R.png"
done

