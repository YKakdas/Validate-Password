# 161101014, Yasar Can Kakdas, Bil 334
#!/usr/bin/env python
import sys
import re

password_file=sys.argv.pop();
output_file=open(password_file[:-4]+'_output.txt','w');
pattern='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])\S{8,}$';
#(?=.*[a-z]) : ensures that at least one lower character
#(?=.*[A-Z]) : ensures that at least one upper character
#(?=.*[0-9]) : ensures that at least one digit
#\S : after ensurances, read characters with this
#{8,} : means at least 8 characters
for line in open(password_file) :
    result=re.findall(pattern,line);
    if(len(result)==0) :
        output_file.write('not valid\n');
    else :
        output_file.write('valid\n');

output_file.close();


