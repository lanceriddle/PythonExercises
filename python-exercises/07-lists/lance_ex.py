#!/usr/bin/env python3

"""
--- LISTS ---
NOTES:
    - You can use a negative index, which counts backwards from the end.
        - items[-1]
    - .append(<item>), .extend(<list>), .insert(<index>, <item>)
    - Slice on array or strings (does not include last index):
        - [2:4] (1-3);  [:4] (0-3);
        - last 2 of a 5-entry list [4:6] (4-5). Alt [-2:].
    - .index()
    - try: except:
    - for <item> in <list_name>:
    - while <condition>:
    - while index < len(animals):
        index += 1
    - <list>.sort(); <new_list> = sorted(<list>)
    - List concat with '+': <list1> + <list2>
    - len(<list>)
    - range(<start_index>, <stop_index+1>, <step_param>) (optional parameters)
        - for number in range(1, len(<list>), 2):
            print(list[number])

"""


## Exercise 1:

def get_item():
    """Retrieves an item from the user."""
    return input("Enter a task for your to­do list. Press <enter> when done: ")

# Initialize the list.")
todo_list = []
list_item = get_item()

# Add to the list.
while  len(list_item) > 0:
    todo_list.append(list_item)
    print("Task added.")
    list_item = get_item()

# Display the list.
print()
print("Your To-Do List:")
print("----------------")
for item in todo_list:
    print(item)


## Alternatively:
"""
finished = False
while not finished:
    list_item = input('Enter a task for your to-do list.  Press <enter> when done: ')
    if len(list_item) == 0:
        finished = True
    else:
        todo_list.append(list_item)
        print('Task added.')
"""
