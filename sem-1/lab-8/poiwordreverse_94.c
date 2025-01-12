#include <stdio.h>
#include <string.h>
int main()
{
    char *ptr1,*ptr2;
    char word[200];
    char copy[200];
    printf("enter word \n");
    gets(word);
    ptr1 = word;
    ptr2 = copy;
    int len = strlen(word);
    for(int i = len-1;i>-1;i--)
    {
        *ptr2 = *(ptr1+i);
        ptr2++;
    }
    puts(copy);

    return 0;
}