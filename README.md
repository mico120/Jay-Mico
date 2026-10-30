# Module 5 - Fundamental Data Structures: Stacks and Queues

## Description
This Python program demonstrates stacks and queues using arrays and linked lists. It includes the required operations, error handling, a menu-driven interface, a balanced-parentheses checker, and a print queue simulation.

## Files
- `stack_array.py` - Array-based stack with push, pop, peek, is_empty, and is_full.
- `stack_linked.py` - Linked-list stack with push, pop, peek, and is_empty.
- `queue_array.py` - Circular array queue with enqueue, dequeue, peek_front, is_empty, and is_full.
- `queue_linked.py` - Linked-list queue with front and rear references.
- `main.py` - Menu-driven program and application exercises.
- `test_driver.py` - Tests the four structures, wrap-around, and error handling.
- `analysis.md` - Written answer to the analysis question.

## Requirements
- Python 3.7 or newer
- No external packages are required.

## How to Run
Open a terminal in this folder and run:

```bash
python main.py
```

Choose an implementation to perform operations, check balanced parentheses, or simulate a print queue.

To run the tests:

```bash
python test_driver.py
```

## Notes
Array implementations use a fixed capacity of 5 in the interactive program. The test driver uses smaller capacities to demonstrate overflow and circular wrap-around. Underflow and overflow are reported with descriptive exceptions.
