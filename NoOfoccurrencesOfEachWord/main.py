import re

String1="This is my test, for testing repeating sentence"
for i in list(dict.fromkeys(re.findall(r'(\w+)',string1))): 
    print(" "+ i + "--" + str(len(re.findall(i,string1))))
