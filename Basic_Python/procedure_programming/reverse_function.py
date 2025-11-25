def reverse(word)


length_word: int= len(word)
i: int = len(word) - 1


while i >= 0:
    print (word[i])
    i -= 1

while i>= 0:
    word1 = word + word[i]
    i -= 1



print(f"{'-'*70}")

word: str = input("enter a word: ").lower()

initial_position: int = len(word) - 1
reversed_word = ""

for index in range ( initial_position, -1 , -1):
    reversed_word = reversed_word + word[index]

print(reversed_word)

