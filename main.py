from stats import get_num_words, get_num_characters, get_sorted_char_count
import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

def get_book_text(book_path):
  with open(book_path) as f:
    return f.read()
  
def main():
  book_text = get_book_text(sys.argv[1])
  num_words = get_num_words(book_text)
  num_characters = get_num_characters(book_text)
  sorted_char_count = get_sorted_char_count(num_characters)

  print("============ BOOKBOT =============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words.")
  print("--------- Character Count -------")
  
  for char in sorted_char_count:
    if char['char'].isalpha():
      print(f"{char['char']}: {char['count']}")

main()