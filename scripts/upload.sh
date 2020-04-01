#!/bin/bash
OUTPUT="/Users/jroesch/Dropbox/OOPSLA19"
if [ -d $OUTPUT ]; then
    NOW=$(date +"%I_%M_%S")
    OLD="${OUTPUT}/*relay_oopsla.pdf"
    echo "Removing: ${OLD}"
    rm $OLD
    NEW="${OUTPUT}/${NOW}_relay_oopsla.pdf"
    echo "Uploading: $NEW"
    cp ./paper.pdf $NEW
    chmod a+w $NEW
fi
