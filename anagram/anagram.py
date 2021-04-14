import itertools
anagram = []
#why not begin from 0? The smallest anagram is always a single character
#why len("python") + 1? To ensure all characters are included in the pattern
for i in range(1, len("python")+1):
    for j in list(itertools.permutations("python", i)):
        anagram.append("".join(j))
        print("".join(j))

print(len(anagram))