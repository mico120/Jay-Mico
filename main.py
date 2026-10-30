from stack_array import ArrayStack
from stack_linked import LinkedStack
from queue_array import ArrayQueue
from queue_linked import LinkedQueue


def choose_structure():
    print("\nChoose an implementation:")
    print("1. Array Stack")
    print("2. Linked List Stack")
    print("3. Circular Array Queue")
    print("4. Linked List Queue")
    choice = input("Choice: ").strip()

    if choice == "1":
        return ArrayStack(5), "stack"
    if choice == "2":
        return LinkedStack(), "stack"
    if choice == "3":
        return ArrayQueue(5), "queue"
    if choice == "4":
        return LinkedQueue(), "queue"
    print("Invalid choice.")
    return None, None


def run_structure(structure, kind):
    while True:
        if kind == "stack":
            print("\n1. Push  2. Pop  3. Peek  4. Is empty  5. Is full  6. Back")
        else:
            print("\n1. Enqueue  2. Dequeue  3. Peek front  4. Is empty  5. Is full  6. Back")
        choice = input("Operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter value: ")
                if kind == "stack":
                    structure.push(value)
                else:
                    structure.enqueue(value)
            elif choice == "2":
                print("Removed:", structure.pop() if kind == "stack" else structure.dequeue())
            elif choice == "3":
                print("Top:" if kind == "stack" else "Front:",
                      structure.peek() if kind == "stack" else structure.peek_front())
            elif choice == "4":
                print("Empty:", structure.is_empty())
            elif choice == "5":
                if hasattr(structure, "is_full"):
                    print("Full:", structure.is_full())
                else:
                    print("Linked-list structures have no fixed capacity.")
            elif choice == "6":
                break
            else:
                print("Invalid operation.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        print("Current state:", structure)


def main():
    while True:
        print("\nSTACKS AND QUEUES")
        print("1. Choose implementation")
        print("2. Parentheses balance checker")
        print("3. Print queue simulation")
        print("4. Exit")
        choice = input("Select: ").strip()

        if choice == "1":
            structure, kind = choose_structure()
            if structure is not None:
                run_structure(structure, kind)
        elif choice == "2":
            expression = input("Enter an expression: ")
            print("Balanced." if is_balanced(expression) else "Not balanced.")
        elif choice == "3":
            simulate_print_queue()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def is_balanced(expression):
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack = []

    for character in expression:
        if character in opening:
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False

    return len(stack) == 0


def simulate_print_queue():
    queue = LinkedQueue()
    print("\nAdd print jobs. Enter a blank job ID to stop adding.")
    while True:
        job_id = input("Job ID: ").strip()
        if not job_id:
            break
        try:
            pages = int(input("Number of pages: "))
            if pages <= 0:
                print("Page count must be positive.")
                continue
        except ValueError:
            print("Please enter a valid page count.")
            continue
        queue.enqueue({"id": job_id, "pages": pages})
        print("Queue:", queue)

    print("\nPrinting jobs in FIFO order:")
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Printing job {job['id']} ({job['pages']} pages)")


if __name__ == "__main__":
    main()
