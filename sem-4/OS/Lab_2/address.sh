#!/bin/bash

FILE="addressbook.txt"

while true
do
    echo "1. Create Address Book"
    echo "2. View Address Book"
    echo "3. Insert Record"
    echo "4. Delete Record"
    echo "5. Modify Record"
    echo "6. Exit"
    read -p "Enter choice: " ch

    case $ch in
        1)
            > "$FILE"
            echo "Address book created"
            ;;
        2)
            if [ -s "$FILE" ]; then
                cat "$FILE"
            else
                echo "Address book is empty"
            fi
            ;;
        3)
            read -p "Name: " name
            read -p "Phone: " phone
            read -p "Email: " email
            echo "$name | $phone | $email" >> "$FILE"
            echo "Record added"
            ;;
        4)
            read -p "Enter name to delete: " name
            grep -v "^$name |" "$FILE" > temp.txt
            mv temp.txt "$FILE"
            echo "Record deleted"
            ;;
        5)
            read -p "Enter name to modify: " name
            grep "^$name |" "$FILE"
            read -p "New Phone: " phone
            read -p "New Email: " email
            grep -v "^$name |" "$FILE" > temp.txt
            echo "$name | $phone | $email" >> temp.txt
            mv temp.txt "$FILE"
            echo "Record modified"
            ;;
        6)
            exit
            ;;
        *)
            echo "Invalid choice"
            ;;
    esac
done
