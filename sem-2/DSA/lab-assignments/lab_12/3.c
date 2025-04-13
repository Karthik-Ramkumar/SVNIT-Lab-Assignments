#include <stdio.h>
#include <stdlib.h>

#define SIZE 10

struct Node {
    int data;
    struct Node *left, *right;
};

struct Node* create_node(int value) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->left = new_node->right = NULL;
    return new_node;
}

int search(int inorder[], int start, int end, int value) {
    for (int i = start; i <= end; i++)
        if (inorder[i] == value) return i;
    return -1;
}

struct Node* build_tree(int inorder[], int preorder[], int in_start, int in_end, int* pre_index) {
    if (in_start > in_end) return NULL;

    int current = preorder[*pre_index];
    (*pre_index)++;
    struct Node* node = create_node(current);

    if (in_start == in_end) return node;

    int in_index = search(inorder, in_start, in_end, current);

    node->left = build_tree(inorder, preorder, in_start, in_index - 1, pre_index);
    node->right = build_tree(inorder, preorder, in_index + 1, in_end, pre_index);

    return node;
}

void inorder_traversal(struct Node* root) {
    if (root == NULL) return;
    inorder_traversal(root->left);
    printf("%d ", root->data);
    inorder_traversal(root->right);
}

void preorder_traversal(struct Node* root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder_traversal(root->left);
    preorder_traversal(root->right);
}

void postorder_traversal(struct Node* root) {
    if (root == NULL) return;
    postorder_traversal(root->left);
    postorder_traversal(root->right);
    printf("%d ", root->data);
}

int main() {
    int inorder[SIZE] = {1, 8, 19, 13, 25, 9, 5, 10, 4, 3};
    int preorder[SIZE] = {25, 8, 1, 13, 19, 5, 9, 4, 10, 3};
    int pre_index = 0;

    struct Node* root = build_tree(inorder, preorder, 0, SIZE - 1, &pre_index);

    printf("Inorder Traversal: ");
    inorder_traversal(root);
    printf("\n");

    printf("Preorder Traversal: ");
    preorder_traversal(root);
    printf("\n");

    printf("Postorder Traversal: ");
    postorder_traversal(root);
    printf("\n");

    return 0;
}
