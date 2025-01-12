#include <stdio.h>
#include <string.h>
int main()
{
    char str[30];
    char *ptr;
    gets(str);
    ptr = str;
    int count,space = 0
    int len = strlen(str);
    for (int i = 0; i < len - 1; i++)
    {
        if (*ptr == ' ')
        {
            space++;
        }
        else
        {
            count++;
        }
        ptr++;
    }
    int spacewith = count + space;
    printf("length without space = %d \n", count);
    printf("length with space = %d \n", spacewith);
}