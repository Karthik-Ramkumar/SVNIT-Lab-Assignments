#include <stdio.h>
int main() 
{
    int N, M;
    printf("enter M and N");
    scanf("%d%d",&N,&M);
    long long total = 0;
    for (int i = 0; i < M; i++) 
    {
        int a, b, k;
        printf("enter a b k");
        scanf("%d%d%d",&a,&b,&k);

        total = (long long )(b-a+1)*k;
    }
    // Calculate  average
    printf(" average is = %lld\n", total / N);
    return 0;
}
