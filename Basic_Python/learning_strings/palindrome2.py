word: str = input("enter a word: ").lower()
length_word = len(word)
flag =  True
"""
range(start, end, step)
0 - len-1
range(0, len//2,) 
"""

for i in range(length_word//2):
    ending_index = length_word - 1 -i
    if word[i].lower() != word[ending_index].lower(): # focus on this part !important
        flag = False
        break

#decision
if flag:
     print(f"Word {word} is a palindrome")
else:
     print(f"Word { word} is not a palindrome")