#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX 100

struct Stack {
    int top;
    int items[MAX];
};

void initStack(struct Stack* s) {
    s->top = -1;
}

int isFull(struct Stack* s) {
    return s->top == MAX - 1;
}

int isEmpty(struct Stack* s) {
    return s->top == -1;
}

void push(struct Stack* s, int value) {
    if (!isFull(s)) {
        s->items[++s->top] = value;
    }
}

int pop(struct Stack* s) {
    if (!isEmpty(s)) {
        return s->items[s->top--];
    }
    return -1;
}

int evaluatePostfix(char* expression) {
    struct Stack s;
    initStack(&s);
    for (int i = 0; expression[i]; i++) 
    {
        if (isdigit(expression[i])) 
        {
            push(&s, expression[i] - '0');
        } 
        else 
        {
            int val2 = pop(&s);
            int val1 = pop(&s);
            switch (expression[i]) 
            {
                case '+':
                    push(&s, val1 + val2);
                    break;
                case '-':
                    push(&s, val1 - val2);
                    break;
                case '*':
                    push(&s, val1 * val2);
                    break;
                case '/':
                    push(&s, val1 / val2);
                    break;
            }
        }
    }
    return pop(&s);
}

int main() {
    char expression[MAX];
    printf("Enter a postfix expression: ");
    scanf("%s", expression);
    printf("Result: %d\n", evaluatePostfix(expression));
    return 0;
}