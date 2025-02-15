"""
Task Prioritization 

As a student, I want to organize my tasks by deadlines and priority so that I can manage my study time efficiently. 

Solution: Allow input of tasks and automatically generate a prioritized schedule. 
"""
# dictionary to sort by priority
# 1 - high prio, 2 - med prio, 3 - low prio.
tasks = {
    1 : [],
    2 : [],
    3 : [],
}

def menu():
    print("Welcome to the Error-Free Calculator! Choose an option:")
    while True:
        try:
            user_choice = int(input("1. Add task \n2. Remove task \n3. See tasks \n4. Exit \n> "))
            if user_choice == 1:
                add_task()
                
            elif user_choice == 2:
                remove_task()
                
            elif user_choice == 3:
                get_tasks()
                
            elif user_choice == 4:
                break
            else:
                print("Invalid input. Please enter a number from the menu...")
        except ValueError:
            print("Invalid input. Please enter a number from the menu...")

def add_task():
    task_name = input("Please enter the name of your task: ")
    while True:
        try:
            task_prio = int(input("""Please enter the priority of your task
    1 for high priority
    2 for medium priority 
    3 for low priority
    : """))
            if task_prio != 1 and task_prio != 2 and task_prio != 3:
                print("Please enter either 1, 2, or 3.")
            else:
                tasks[task_prio].append(task_name)
                print(f"""Added "{task_name}" with a priority of {task_prio}.""")
                break
        except ValueError:
            print("That's not a valid number! Please enter a valid number...")

def remove_task():
    while True:
        try:
            task_prio = int(input("Please enter priority menu number you want to remove from (1-3): "))
            if task_prio != 1 and task_prio != 2 and task_prio != 3:
                print("Please enter either 1, 2, or 3.")
            else:
                if len(tasks[task_prio]) == 0:
                    print("No tasks in this list.")
                    break
                for i in range(len(tasks[task_prio])):
                    print(f"{i+1}. {tasks[task_prio][i]}")
                while True:
                    try:
                        task_num = int(input("Please enter the task number you want to remove: "))
                        if task_num < 1 or task_num > len(tasks[task_prio]):
                            print("Please enter a valid task index...")
                        else:
                            print(f"""Removed "{tasks[task_prio][task_num-1]}".""")
                            tasks[task_prio].pop(task_num-1)
                            break
                    except ValueError:
                        print("That's not a valid number! Please enter a valid number...")
                break
        except ValueError:
            print("That's not a valid number! Please enter a valid number...")


def get_tasks():
    print("Here's a list of your tasks:")
    for key in tasks:
        if key == 1:
            print("High priority:")
        elif key == 2:
            print("Medium priority:")
        else:
            print("Low priority:")
        print(tasks[key])


# Performance Tracking

subjects = {}

def add_subject():
    subject = input("Please enter the name of the new subject you would like to add: ")
    if subject in subjects:
        print("This subject already exists.")
    else:
        subjects[subject] = []
        print(f"""Added "{subject}" to subjects.""")
    
def add_score():
    print("Subjects:")
    for key in subjects:
        print(key)
    subject = input("Please enter the subject you want to add a score to: ")
    if subject in subjects:
        while True:
            try:
                score = int(input("Enter your score: "))
                subjects[subject].append(score)
                break
            except ValueError:
                print("Please enter a valid score...")
    else:
        print("Subject does not exist.")

def show_scores():
    print(subjects)
