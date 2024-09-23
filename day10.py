#  group all the strings that are anagrams of each other

strs= ["abc", "def", "ghi","tan","ant2"]
group_anagrams=[]

while strs:
    s=strs[0]
    characters=sorted(list(s))
    anagram=[]
    for j in strs:
        if sorted(list(j))==characters:
            anagram.append(j)
    group_anagrams.append(anagram)

    for i in anagram:
        strs.remove(i)

print(group_anagrams)
    
