#!/bin/bash

IFS=$'\012'

FULLURL=https://www.networkrail.co.uk/who-we-are/transparency-and-ethics/transparency/our-information-and-data/

if [ ! -s index.html ]; then
    curl -o index.html ${FULLURL}
fi

for FILE in data output
do
    if [ ! -d ${FILE} ]; then
        mkdir ${FILE}
    fi
done

for DATA in $(./htmltojson.py index.html --depth 12 --stdout | ./25kfilter.py)
do
    FILEURL=$(echo ${DATA} | jq -r '.url')
    FILENAME=$(echo ${DATA} | jq -r '.name')
    FILESTUB=$(echo ${FILENAME} | sed 's/.xlsx$//')
    if [ ! -s data/${FILENAME} ]; then
        curl -o data/${FILENAME} ${FILEURL}
    fi
    $(ls output/${FILESTUB}*.tsv 2> /dev/null) || ./xl2tsv.py --sourcename data/${FILENAME}
done

