def check_palindrome(word):
    word = word.lower()
    length_word = len(word)
    flag = True

    for i in range(length_word // 2):
        ending_index = length_word - 1 - i
        if word[i].lower() != word[ending_index].lower():
            flag = False
            break

    return flag


word = input("enter a word:")
result = check_palindrome(word)

if result:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")