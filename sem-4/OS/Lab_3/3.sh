#!/bin/bash

read -p "Enter words: " -a words

for w in "${words[@]}"
do
    echo "$w length = ${#w}"
done
