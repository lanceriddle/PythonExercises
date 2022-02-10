#!/usr/bin/env python3

import os

"""
--- FILES ---
NOTES:
    file = open(<path>) #(Absolute or Relative) (Forward or Backward slashes)
    contents = file.read() #or .read(<num_chars_to_read>)
    .seek(<byte_offset_from_file_start>) #e.g. restart by .seek(0)
    .tell() (Current position in file)
    .close()
    .closed # Returns boolean for if file is closed or not
    
    # Automatically Closing a File
    with open(<file_path>) as file:
        # Code block, Python will close file after this.
    
    # Read file line-by-line, use for-loop.
    with open(<file_path>) as the_file:
        for line in the_file:
            print(line.rstrip()) # Without "rstrip()", this would include carriage returns on each line.

    # Modes:
    open(<path>, <mode>)
        - r: Reading (Default)
        - w: Writing/Creating, clears existing contents first
        - x: Create a new file and open it for writing (if file exists, exception thrown)
        - a: Open/Creating for writing, appending to file
        - +: Read and Write mode
    Formats:
        - b: Binary mode (.read() accepts bytes)
        - t: Text mode (Default) (.read() accepts characters)
    
    file.mode returns open mode.
    
    file.write(<text_to_write>)
    
    # Carriage Returns and Line Feeds
    \r: Carriage Return
    \n: New Line
    \n: Unix/Linux/Mac line endings
    \r\n: Windows line endings
    
    - Use try: except: blocks in case file can't be opened or written to.

"""

## EXERCISE 1
## **********
print()
print()
print("EXERCISE 1")
print()

# Find the file in the same path as the currently executing .py file.
target_path = os.path.join(os.path.dirname(__file__), 'file.txt')

try:
    with open(target_path) as file:
        line_count = 1
        for line in file:
            print("{}: {}".format(line_count, line.rstrip()))
            line_count += 1
except:
    print("Error processing file.")



## EXERCISE 2
## **********
print()
print()
print("EXERCISE 2")
print()

# Find the file in the same path as the currently executing .py file.
input_path = os.path.join(os.path.dirname(__file__), 'animals.txt')
output_path = os.path.join(os.path.dirname(__file__), 'animals-sorted.txt')
list = []

try:
    # Read list of animals:
    with open(input_path) as file:
        for line in file:
            list.append(line.rstrip())
    print("Read: {}".format(list))

    # Sort list:
    list.sort()
    print("Sorted: {}".format(list))

    # Write list:
    with open(output_path, "w") as output_file:
        for item in list:
            print("{}".format(item))
            output_file.write("{}\n".format(item))
except:
    print("Error processing file.")
