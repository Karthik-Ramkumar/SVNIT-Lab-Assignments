#include <stdio.h>
void oddoreven(int num) {
    if (number % 2 == 0) {
        printf("%d is even.\n", number);
    } else {
        printf("%d is odd.\n", number);
    }
}

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    oddoreven(num);

    return 0;
}
