# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

s="percussion supersonic car tree boy girl arc"

list=[]
list=s.split()
print(list)

anagram_list=[]

for item in list:
    for item_2 in list:
        if item!=item_2 and sorted(item)==sorted(item_2):
               anagram_list.append(item+" and "+item_2)

print(anagram_list)