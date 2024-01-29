def main():
   book_path = "books/frankenstein.txt"
   text = get_text(book_path)
   num_words = word_count(text)
   char_dict = character_count(text)
   char_list = sorted(char_dict, key=char_dict.get, reverse=True)
   print(f"--- Begin report of {book_path}")
   print(f"{num_words} words found in the document")
   for char in char_list:
       if char.isalpha():
           print(f"The {char} character was found {char_dict[char]} times")
   print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    counts = {}
    for char in text:
        lowered = char.lower()
        if lowered in counts:
            counts[lowered] += 1
        else:
            counts[lowered] = 1
    return counts

def get_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()