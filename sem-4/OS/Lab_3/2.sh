#!/bin/bash

file_path="file_path"

if [ -e "$file_path" ]; then
    echo "$file_path passwords are enabled."
    if [ -w "$file_path" ]; then
        echo "You have permissions to edit $file_path."
    else
        echo "You do NOT have permissions to edit $file_path"
    fi
fi
