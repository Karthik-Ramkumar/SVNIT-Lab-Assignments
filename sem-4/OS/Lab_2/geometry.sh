#!/bin/bash

echo "1. Area of Circle"
echo "2. Circumference of Circle"
echo "3. Area of Rectangle"
echo "4. Area of Square"
read -p "Enter choice: " choice

case $choice in
1)
    read -p "Enter radius: " r
    echo "Area = $(echo "3.14 * $r * $r" | bc)"
    ;;
2)
    read -p "Enter radius: " r
    echo "Circumference = $(echo "2 * 3.14 * $r" | bc)"
    ;;
3)
    read -p "Enter length: " l
    read -p "Enter breadth: " b
    echo "Area = $(echo "$l * $b" | bc)"
    ;;
4)
    read -p "Enter side: " s
    echo "Area = $(echo "$s * $s" | bc)"
    ;;
*)
    echo "Invalid choice"
    ;;
esac
