#!/bin/bash

read -p "Enter sorted numbers: " -a arr
read -p "Enter number to search: " key

low=0
high=$((${#arr[@]}-1))
found=0

while [ $low -le $high ]
do
    mid=$(((low+high)/2))
    if [ ${arr[$mid]} -eq $key ]; then
        echo "Found at position $mid"
        found=1
        break
    elif [ ${arr[$mid]} -lt $key ]; then
        low=$((mid+1))
    else
        high=$((mid-1))
    fi
done

[ $found -eq 0 ] && echo "Not found"
