#
# You are tasked with developing an advanced task management system that can handle multiple users, prioritize tasks, and track task completion. The system will be used by a project management team to coordinate tasks and monitor progress.
#
# Your task is to create a class called TaskManager that will utilize the following data structures and classes:
#
# •	ChainMap: This data structure will be used to combine multiple dictionaries into a single dictionary. In our case, we will use it to combine user-wise task dictionaries into a single dictionary.
#
# •	Counter: This class will help us count the number of tasks in each category for each user. It will be used to keep track of the task counts for each user and category.
#
# •	deque: This data structure will be used to maintain a queue of tasks. Whenever a new task is created, it will be added to the deque. When a task is completed or removed, it will be removed from the deque.
#
# •	defaultdict: This class will be used to create a dictionary with a default value. In our case, we will use it to create a dictionary that automatically assigns an empty deque to a new user when it is encountered for the first time.
#
# •	namedtuple(): This function will be used to create a class called Task that will represent a single task. It will have attributes such as name, user, category, description, and priority.
#
# •	OrderedDict: This class will be used to create an ordered dictionary that will preserve the order of task creation. Whenever a new task is added, it will be appended to the end of the ordered dictionary.
#
# Now, create the TaskManager class with the following methods:
#
# •	__init__(): Initializes the task manager by creating the necessary data structures.
# •	add_task(task): Adds a new task to the task manager. The task should be an instance of the Task class. The method should update the user-wise task dictionary, increment the task count for the corresponding user and category, and add the task to the end of the ordered dictionary.
# •	remove_task(task_name): Removes a task from the task manager based on its name. The method should remove the task from the user-wise task dictionary, decrement the task count for the corresponding user and category, and remove the task from the ordered dictionary.
# •	get_task_count(user, category): Returns the number of tasks in a given category for a specific user.
# •	get_task_list(user, category): Returns a list of tasks in a given category for a specific user, ordered by their creation.
# •	complete_task(task_name): Marks a task as completed. The method should remove the task from the user-wise task dictionary, decrement the task count for the corresponding user and category, and remove the task from the ordered dictionary.
# •	get_completed_tasks(user): Returns a list of completed tasks for a specific user, ordered by their completion.
#
# Note: Remember to import the necessary modules and classes at the beginning of your code.

from collections import ChainMap, Counter, deque, defaultdict, namedtuple, OrderedDict

Task = namedtuple('Task', ['name', 'user', 'category', 'description', 'priority'])


class TaskManager:
    def __init__(self):
        self.user_tasks = defaultdict(deque)
        self.task_counts = defaultdict(Counter)
        self.task_list = OrderedDict()

    def add_task(self, task):
        self.user_tasks[task.user].append(task)
        self.task_counts[task.user][task.category] += 1
        self.task_list[task.name] = task
        print(f"Task '{task.name}' added.")

    def remove_task(self, task_name):
        if task_name in self.task_list:
            task = self.task_list.pop(task_name)
            self.user_tasks[task.user].remove(task)
            self.task_counts[task.user][task.category] -= 1
            print(f"Task '{task.name}' removed.")
        else:
            print(f"Task '{task_name}' not found.")

    def get_task_count(self, user, category):
        return self.task_counts[user][category]

    def get_task_list(self, user, category):
        return [task for task in self.user_tasks[user] if task.category == category]

    def complete_task(self, task_name):
        if task_name in self.task_list:
            task = self.task_list.pop(task_name)
            self.user_tasks[task.user].remove(task)
            self.task_counts[task.user][task.category] -= 1
            print(f"Task '{task.name}' marked as completed.")
        else:
            print(f"Task '{task_name}' not found.")

    def get_completed_tasks(self, user):
        return [task for task in self.task_list.values() if task.user == user and task.name not in self.task_list]

# Testing the TaskManager class
tm = TaskManager()

# Adding tasks
task1 = Task('Task 1', 'User A', 'Category A', 'Do something', 'High')
task2 = Task('Task 2', 'User B', 'Category B', 'Do something else', 'Low')
task3 = Task('Task 3', 'User A', 'Category A', 'Do another thing', 'Medium')

tm.add_task(task1)
tm.add_task(task2)
tm.add_task(task3)

# Getting task counts
print(tm.get_task_count('User A', 'Category A')) # 2
print(tm.get_task_count('User B', 'Category B')) # 1


# Getting task lists
print(tm.get_task_list('User A', 'Category A'))
print(tm.get_task_list('User B', 'Category B'))
# Completing a task
tm.complete_task('Task 1')

# Getting updated task counts and lists

print(tm.get_task_count('User A', 'Category A')) # 1
print(tm.get_task_count('User B', 'Category B')) # 1

print(tm.get_task_list('User A', 'Category A'))


# Getting completed tasks
print(tm.get_completed_tasks('User A'))
print(tm.get_completed_tasks('User B'))