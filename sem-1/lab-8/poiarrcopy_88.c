#include <stdio.h>
#include <string.h>
int main()
{
    char ar1[30];
    char ar2[30];
    char *ptr1;
    char *ptr2;
    printf("Enter string \n");
    ptr1 = ar1;
    ptr2 = ar2;
    // fgets(ar1, sizeof(ar1), stdin);
    gets(ar1);
    while (*ptr1 != '\0')
    {
        *ptr2 = *ptr1;
        ptr1++;
        ptr2++;
    }
    *ptr2 = '\0';
    printf("After copying  \n");
    puts(ar2);
    return 0;
}
