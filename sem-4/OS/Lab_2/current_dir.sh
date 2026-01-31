#!/bin/bash

date=$(date +%Y-%m-%d)

for file in *.jpg; do
    [ -e "$file" ] || continue
    mv "$file" "$date-$file"
done
