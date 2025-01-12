/*#include <stdio.h>
#include <string.h>
int main()
{
    int i,j,k,count;
    int n = 0;
    
    printf("enter number of elements\n");
    scanf("%d",&n);
    char rock[n][10];
    char gems[26]={0}; //number of letters is 26
    //-------------------------------------
    printf("enter rock compositions\n");//taking rock inputs
    for(int i =0; i<n;i++)
    {
        scanf("%s",rock[i]);
    }
    for(int j =0; j<n;j++) //printing rock compositions
    {
        printf("rock : %s \t",rock[j]);
    }
    printf("\n");
    //----------------------------element management
    for(i = 0;i<n;i++)
    {
        for (int j = 0;j < strlen(rock[i]);j++)
        {
            gems[rock[i][j] - 'a'] = 1; // mark element as present
            /*for(k = 0;k<length[i];k++)
            {
                if(rock[i][j]!= store[k])
                {
                store[k] = rock[i][j];
                count = count+1;
                }
            }*/
       /* }
                for (int k = 0; k < 26; k++) 
        {
            if (gems[k] == 1) 
            {
                gem_count[k]++;
            }
        }
    }*/
    //-------------------------------------------
    /*printf("distinc elements are:\n");      
    for(i=0;i<count;i++)
    {
        printf("\n %c",store[i]);
    }
    return 0;*/
            // Increment gem_count for elements present in this rock

    

    // Count how many elements are common to all rocks*/
    /*int common_elements = 0;
    for (int i = 0; i < 26; i++)
    {
        if (gem_count[i] == n) 
        {
            common_elements++; // element is common in all rocks
        }
    }
    printf("Number of gem-elements: %d\n", common_elements);
    return 0;

}*/
#include <stdio.h>
#include <string.h>
int main()
{
    int n;
    printf("Enter the number of rocks:\n");
    scanf("%d", &n);
    char rock[n][10];
    int gem_count[26] = {0};
    printf("Enter the compositions of each rock:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%s", rock[i]);
    }
    //---------------------------------------------------
    // Checking each rock's elements to find uniQue elements
    for (int i = 0; i < n; i++)
    {
        char gems[26] = {0}; 
        for (int j = 0;j < strlen(rock[i]);j++)
        {
            gems[rock[i][j] - 'a'] = 1; // Mark presence of element
        }
        // Increment gem_count for elements present in this rock
        for (int j = 0; j < 26; j++)
        {
            if (gems[j] == 1)
            {
                gem_count[j]++;
            }
        }
    }
    // Count how many elements are common to all rocks
    int common_elements = 0;
    for (int i = 0; i < 26; i++)
    {
        if (gem_count[i] == n)
        {
            common_elements++;
        }
    }
    printf("Number of gem-elements: %d\n", common_elements);
    return 0;
}
