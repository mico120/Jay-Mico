from stack_array import ArrayStack
from stack_linked import LinkedStack
from queue_array import ArrayQueue
from queue_linked import LinkedQueue
from main import is_balanced


def test_array_stack():
    stack = ArrayStack(2)
    stack.push("A")
    stack.push("B")
    assert stack.peek() == "B"
    assert stack.pop() == "B"
    assert stack.pop() == "A"
    try:
        stack.pop()
    except IndexError as error:
        print("Array stack underflow handled:", error)
    stack.push("X")
    stack.push("Y")
    try:
        stack.push("Z")
    except OverflowError as error:
        print("Array stack overflow handled:", error)


def test_linked_stack():
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.pop() == 10
    print("Linked stack test passed.")


def test_array_queue():
    queue = ArrayQueue(3)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.dequeue() == "A"
    queue.enqueue("D")
    print("Circular queue after wrap-around:", queue)
    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"
    assert queue.dequeue() == "D"
    try:
        queue.dequeue()
    except IndexError as error:
        print("Array queue underflow handled:", error)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    try:
        queue.enqueue(4)
    except OverflowError as error:
        print("Array queue overflow handled:", error)


def test_linked_queue():
    queue = LinkedQueue()
    queue.enqueue("First")
    queue.enqueue("Second")
    assert queue.peek_front() == "First"
    assert queue.dequeue() == "First"
    assert queue.dequeue() == "Second"
    assert queue.is_empty()
    queue.enqueue("After empty")
    assert queue.dequeue() == "After empty"
    print("Linked queue test passed, including empty-queue reset.")


def test_parentheses():
    assert is_balanced("([{}])")
    assert not is_balanced("([)]")
    assert not is_balanced("(((")
    print("Parentheses checker tests passed.")


if __name__ == "__main__":
    test_array_stack()
    test_linked_stack()
    test_array_queue()
    test_linked_queue()
    test_parentheses()
    print("\nAll tests passed.")
