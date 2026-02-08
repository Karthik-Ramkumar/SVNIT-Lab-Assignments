#!/bin/bash
read -p "Enter count: " n
echo "Enter numbers:"
read -a arr
max=${arr[0]}
for num in "${arr[@]}"
do
    if [ $num -gt $max ]; then
        max=$num
    fi
done
echo "Largest = $max"
