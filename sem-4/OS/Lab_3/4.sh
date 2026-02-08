#!/bin/bash

read -p "Enter five digit number: " num
rev=0

while [ $num -gt 0 ]
do
    d=$((num%10))
    rev=$((rev*10+d))
    num=$((num/10))
done

echo "Reversed = $rev"
