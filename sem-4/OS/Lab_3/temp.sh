#!/bin/bash

read -p "enter a word to check if it is a palindrom: " word

rev=$(echo "$word" | rev)

if [ "$word" = "$rev" ]
then
    echo "it is a palindrom"
else
    echo "the word is not a palindrome"
fi


