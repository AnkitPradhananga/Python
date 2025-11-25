word : str = input("enter a word:")#.lower() for case independence
letter: str = input("enter a letter:")#.lower() for case independence

if len(letter) > 1:
    print("letter is too long.Must be one character")
    exit(1)

length_word: int = len(word)
i: int = 0
index: int = -1

#printing the word char by char
while i < length_word:
     if word[i] == letter:
        index = i
        break

     i += 1



if index != -1:
    print(f"Value found at index: {index}")
else:
    print(f"Value not found at index: {word}")

print(f"{'-'*50}")