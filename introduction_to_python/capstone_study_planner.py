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

def add_task():
    task_name = input("Please enter the name of your task: ")
    task_prio = int(input("""Please enter the priority of your task
    1 for high priority
    2 for medium priority 
    3 for low priority
    : """))

add_task()