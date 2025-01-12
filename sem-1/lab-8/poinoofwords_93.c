#include <stdio.h>
#include <string.h>
int main()
{
    char *ptr;
    char words[200];
    printf("enter sentence \n");
    gets(words);
    int len = strlen(words);
    int count = 1;
    ptr = words;
    for(int i = 0;i<len-1;i++)
    {
        if(*ptr == ' ')
        {
            count++;
        }
        ptr++;
    }
    printf("number of words = %d",count);
    return 0;
}