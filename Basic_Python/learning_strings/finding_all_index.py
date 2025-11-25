'''
takes a word from the user
take a letter from the user

find all the occurences of the letter i the word
'''

word: str = input("enter a word: ")
letter: str = input("enter a letter: ")
indexes: list[int] = list() # or [] same thing

if len(letter) != 1:
    print(f"please enter a letter within the word: {word}. Letter cannot be empty")
    exit(3)

"""
for<storage> in <iterator>:
{BL}

enumerate(<iterator>)  -> enumerate(sahil) -> (0,s),(1,a),(2,h),(.....

Iter 1:
index,character -> (0,s)  # tuple destructuring

letter: l
enumerate(<iterator>)  -> enumerate(sahil lodha) -> (0,s),(1,a),(2,h),(.....

Iter 5:
index,character -> (4,l)   # tuple destructuring
if case: [].append(4) -> indexes:[4]

Iter 7:
index,character -> (6,l)   # tuple destructuring
if case: [4].append(6) -> indexes:[4,6]



"""

for index, character in  enumerate(word):
    '''
    how does thi word?
    index,character garne karan k cha ra yaha
    '''
    if character.lower() == letter.lower():
        indexes.append(index)

if indexes:
    print(f"Letter {letter} found at index {indexes}")
else:
    print(f"Letter {letter} not found in {word}")
