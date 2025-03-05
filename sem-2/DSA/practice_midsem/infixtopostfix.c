#include <stdio.h>
#include <ctype.h>

#define MAX 50

char stack[MAX];
int top = -1;

void push(char c) {
    stack[++top] = c;
}

char pop() {
    return (top == -1) ? -1 : stack[top--];
}

int precedence(char c) {
    if (c == '+' || c == '-') return 1;
    if (c == '*' || c == '/') return 2;
    if (c == '^') return 3;  // Highest precedence
    return 0;
}

void infixToPostfix(char *infix) {
    char *p = infix, ch;
    while (*p) {
        if (isalnum(*p))  
            printf("%c", *p);
        else if (*p == '(')
            push(*p);
        else if (*p == ')') {
            while ((ch = pop()) != '(')
                printf("%c", ch);
        } else {  // Operator found
            while (top != -1 && precedence(stack[top]) >= precedence(*p))
                printf("%c", pop());
            push(*p);
        }
        p++;
    }
    while (top != -1)  
        printf("%c", pop());
}

int main() {
    char infix[MAX];
    printf("Enter infix expression: ");
    scanf("%s", infix);
    printf("Postfix: ");
    infixToPostfix(infix);
    return 0;
}
