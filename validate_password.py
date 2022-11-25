# !/usr/bin/env python
import os
import re
import sys

if not len(sys.argv) > 1:
    print("Could not find a text file that contains passwords to be validated")
    exit(0)

password_file = sys.argv.pop()

if not os.path.exists(password_file):
    print("Could not find the specified file named: " + password_file)
    exit(0)

output_file = open(password_file[:-4] + '_output.txt', 'w')
pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])\S{8,}$'
# (?=.*[a-z]) : ensures that at least one lower character
# (?=.*[A-Z]) : ensures that at least one upper character
# (?=.*[0-9]) : ensures that at least one digit
# \S : after satisfying the constraints, read any character but whitespace with this
# {8,} : means at least 8 characters

for line in open(password_file):
    result = re.findall(pattern, line)
    if len(result) == 0:
        output_file.write('Password: \"' + line.replace("\n", "") + '\" is not valid\n')
    else:
        output_file.write('Password: \"' + line.replace("\n", "") + '\" is valid\n')

output_file.close()
