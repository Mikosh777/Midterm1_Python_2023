
def tax_calculator():
    name = input("Enter your name please: ")
    while True:
        try:
            salary = float(input("Enter your desired salary level: "))
            break
        except ValueError:
            print("Please enter your desired salary as a digit.")
    tax = salary * 0.2 
    print(f"{name}, the tax level you will pay with the salary {salary} is {tax}")


def calculator():
    operations = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
        3: lambda x, y: x / y,
        4: lambda x, y: x ** y
    }
    print("Please choose the task you want to perform:")
    print("1. Addition\n2. Multiplication\n3. Division\n4. Exponentiation")
    
    try:
        task = int(input())
        if task not in operations:
            raise ValueError
        numbers = input("Please enter two numbers, comma separated: ").split(",")
        if len(numbers) != 2:
            raise ValueError
        x, y = map(float, numbers)
        result = operations[task](x, y)
        print(result)
    except (ValueError, ZeroDivisionError):
        print("Invalid input or operation.")


def fibonacci_sequence():
    try:
        n = int(input("Please enter the length of Fibonacci sequence: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a positive integer.")
        return
    
    fibonacci_sequence = [1, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(f"The Fibonacci sequence for {n} is {', '.join(map(str, fibonacci_sequence))}")


def unique_items():

    items = input("Please enter items separated by comma: ").split(", ")
    unique_items = set(items)
    non_unique_items = [(item, items.count(item)) for item in set(items) if items.count(item) > 1]
    
    print("Items are saved")
    print(f"Unique items: {unique_items}")
    print(f"Not unique items: {tuple(non_unique_items)}")


def to_do_list_manager():
    tasks = []
    completed_tasks = []
    while True:
        print("\nPlease choose the task you want to perform:")
        print("1. Add Task\n2. View All Tasks\n3. Mark Task as Completed\n4. View All Completed Tasks\n5. Exit")
        try:
            choice = int(input())
            if choice < 1 or choice > 5:
                raise ValueError
        except ValueError:
            print("Invalid choice, please try again.")
            continue
        
        if choice == 1:
            task = input("Enter the task: ")
            tasks.append(task)
            print(f'The task "{task}" was added to the todo list')
        elif choice == 2:
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nAll Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
        elif choice == 3:
            if not tasks:
                print("No tasks in the list.")
            else:
                task = input("Enter the name of the task: ")
                if task in tasks:
                    tasks.remove(task)
                    completed_tasks.append(task)
                    print(f'The task "{task}" is marked as completed')
                else:
                    print(f'Task "{task}" not found in the list')
        elif choice == 4:
            if not completed_tasks:
                print("No completed tasks.")
            else:
                print("\nCompleted Tasks:")
                for index, task in enumerate(completed_tasks, 1):
                    print(f"{index}. {task}")
        elif choice == 5:
            break

if __name__ == "__main__":         
    print('\nTask 1')               
    tax_calculator()                
    print('\nTask 2')
    calculator()
    print('\nTask 3')
    fibonacci_sequence()
    print('\nTask 4')
    unique_items()
    print('\nTask 5')
    to_do_list_manager()