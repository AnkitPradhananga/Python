word: str = input("Enter a word: ").lower()


i = len(word) - 1
reversed_word = ""

while i >= 0:
    reversed_word = reversed_word + word[i]
    i -= 1


if reversed_word == word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is NOT a palindrome.")
