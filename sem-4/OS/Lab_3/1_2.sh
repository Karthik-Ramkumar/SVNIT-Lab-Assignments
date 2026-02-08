#!/bin/bash
read -p "Enter first value: " a
read -p "Enter second value: " b
temp=$a
a=$b
b=$temp
echo "After swap: a=$a b=$b"
