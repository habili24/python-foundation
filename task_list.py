tasks = []

print("Welcome to your Task List")

while True:
    task = input("Enter a task (or type 'quit' to exit): ")

    if task.lower() == "quit":
        print("\nYour tasks:")
        for t in tasks:
            print("- " + t)
        break

    tasks.append(task)
    print("Task added.\n")
