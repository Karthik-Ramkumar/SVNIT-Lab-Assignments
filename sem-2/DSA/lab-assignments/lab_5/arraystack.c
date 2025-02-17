#include <iostream>
#define MAXSIZE 100

struct Stack 
{
    int stArr[MAXSIZE];
    int top;
};

void create(Stack &s) 
{
    s.top = -1;
}

bool isFull(Stack &s) 
{
    return s.top == MAXSIZE - 1;
}

bool isEmpty(Stack &s) 
{
    return s.top == -1;
}

void push(Stack &s, int value)
 {
    if (isFull(s)) 
    {
        std::cout << "Stack is full!\n";
        return;
    }
    s.stArr[++s.top] = value;
}

int pop(Stack &s) 
{
    if (isEmpty(s)) 
    {
        std::cout << "Stack is empty!\n";
        return -1;
    }
    return s.stArr[s.top--];
}

int peek(Stack &s) 
{
    if (isEmpty(s)) 
    {
        std::cout << "Stack is empty!\n";
        return -1;
    }
    return s.stArr[s.top];
}

int main() 
{
    Stack s;
    create(s);
    
    push(s, 10);
    push(s, 20);
    push(s, 30);
    
    std::cout << "Top element: " << peek(s) << "\n";
    std::cout << "Popped: " << pop(s) << "\n";
    std::cout << "Stack empty: " << (isEmpty(s) ? "Yes" : "No") << "\n";
    
    return 0;
}