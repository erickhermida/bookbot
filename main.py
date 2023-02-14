with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
word_count = len(words)

text = file_contents.lower()
letters = {}

def get_letters_only(text):
    new_text = []
    acceptable_letters = "abcdefghijklmopqrstuvwxyz"

    for char in text:
        for acceptable in acceptable_letters:
            if char == acceptable:
                new_text.append(char)

    return new_text

new_text = get_letters_only(text)

for char in new_text:
    letters[char] = 0

for char in new_text:
    letters[char] = letters[char] + 1

sorted_letters = letters.items()

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")

for set in sorted_letters:
    print(f"The {set[0]} character was found {set[1]} times")

print("--- End Report ---")