#include <stdio.h>
#include <string.h>

int main()
{
    printf("enter word");
    /*char word[10] = "";
    puts(word);*/
    char word[100] = "gfedcba";
    int len = strlen(word);
    int flag = 0;
    for (int i = 0; i < len-1; i++)
    {
        if (word[i] < word[i+1])
        {
            char temp = word[i];
            word[i] = word[i+1];
            word[i+1] = temp;
            flag = 1;
            break;
        }
    }
    
    if(flag == 1)
    {
    printf("The lexicographically bigger word is: ");
    for (int i = 0; i < len; i++)
    {
        printf("%c", word[i]);
    }
    }
    else
    {
        printf("there is no bigger lexicographical Pattern.");
    }

    return 0;
}
