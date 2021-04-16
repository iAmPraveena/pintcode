### Questions:

*Why are we using dict.fromkeys?*

The findall method returns all the string tokens as list, which might contain duplicates. The dict.fromkeys method returns a unique set of keys of from the input list.

*Why are we typecasting to str?*

The len() method returns an integer object which contains the length.

*Output:*
```
>>> string1="This is my test, for testing repeating sentence"
 >>> for i in list(dict.fromkeys(re.findall(r'(\w+)',string1))):
 ...     print(i + "--" + str(len(re.findall(i,string1))))
 ... 
  testing--1
  is--2
  test--2
  repeating--1
  This--1
  sentence--1
  my--1
  for--1
 >>>  
```
