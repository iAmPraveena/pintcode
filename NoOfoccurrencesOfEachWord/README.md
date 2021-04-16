### Questions:

*Why are we using dict.fromkeys?*

The findall method returns all the string tokens as list, which might contain duplicates. The dict.fromkeys method returns a unique set of keys of from the input list.

*Why are we typecasting to str?*

The len() method returns an integer object which contains the length.
