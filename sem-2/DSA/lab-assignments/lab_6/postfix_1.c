#include <stdio.h>

#define MAX 100

char stack[MAX];
int top = -1;

void push(char c) 
{
    if (top < MAX - 1) 
    {
        stack[++top] = c;
    }
}

char pop() 
{
    return (top >= 0) ? stack[top--] : '#';
}

char peek() 
{
    return (top >= 0) ? stack[top] : '#';
}

int precedence(char c) 
{
    if (c == '+' || c == '-') return 1;
    if (c == '*' || c == '/') return 2;
    return 0;
}

void infixToPostfix(char *exp) 
{
    int i = 0;
    while (exp[i] != '\0') 
    {
        if ((exp[i] >= 'A' && exp[i] <= 'Z') || (exp[i] >= 'a' && exp[i] <= 'z')) 
        {
            printf("%c", exp[i]);
        } 
        else if (exp[i] == '(') 
        {
            push(exp[i]);
        } else if (exp[i] == ')') 
        {
            while (top >= 0 && peek() != '(') 
            {
                printf("%c", pop());
            }
            pop();
        } 
        else 
        {
            while (top >= 0 && precedence(peek()) >= precedence(exp[i])) 
            {
                printf("%c", pop());
            }
            push(exp[i]);
        }
        i++;
    }
    while (top >= 0) 
    {
        printf("%c", pop());
    }
}

int main() 
{
    char expression[MAX];
    printf("Enter infix expression: ");
    scanf("%s", expression);
    printf("Postfix expression: ");
    infixToPostfix(expression);
    return 0;
}