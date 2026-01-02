#! /bin/sh

echo Converting image files to avif

for FILE in *.avif *.png *.jpeg; do
    #echo $FILE
    filename=$FILE

    echo Coverting $FILE to ${filename%.*}'.webp'
    magick $FILE ${filename%.*}'.webp'

done
