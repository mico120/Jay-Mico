# Analysis Question

The linked-list stack pushes at the head because the head can be updated directly, making insertion an O(1) operation. Pushing at the tail would require traversing the list to find the last node, which takes O(n) time in a singly linked list. The array queue must be circular so that positions freed by dequeue operations at the beginning of the array can be reused. The modulo operator allows the front and rear positions to wrap around to the start of the array without shifting the remaining elements.
