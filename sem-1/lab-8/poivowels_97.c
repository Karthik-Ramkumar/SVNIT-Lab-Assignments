#include <stdio.h>
#include <string.h>
int main()
{
    char *ptr1;
    char word[200];
    int count = 0;
    printf("enter sentence \n");
    gets(word);
    ptr1 = word;
    int len = strlen(word);
    for(int i = len-1;i>-1;i--)
    {
        switch (*ptr1)
        {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            {
                count++;
                ptr1++;
            }
            default:
            {
               ptr1++; 
            }
        }
    }
    printf("number of vovewles = %d",count);

    return 0;
}