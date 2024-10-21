#Python Exercise
'''
45. Write a Python program that calls an external command.
'''

#Solution

import subprocess

# Running the command and capturing the output
result = subprocess.run(['dir'], text=True,shell=True)
result.stdout