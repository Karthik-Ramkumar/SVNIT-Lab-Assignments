#include <stdio.h>
#include <string.h>
int main()
{
    char ar1[30];
    char ar2[30];
    char *ptr1;
    char *ptr2;
    ptr1 = ar1;
    ptr2 = ar2;    
    printf("enter string \n");
    gets(ar1);
    int len = strlen(ar1);
    for(int i = len-1; i>-1;i--)
    {
        *ptr2 = ar1[i];
        ptr2++;
    }
    *ptr2 = '\0';
    printf("After copying  \n");
    puts(ar2);
    return 0;
}