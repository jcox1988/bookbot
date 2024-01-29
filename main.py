def main():
   book_path = "books/frankenstein.txt"
   text = get_text(book_path)
   num_words = word_count(text)
   print(f"{num_words} words found in the document")
   print(character_count(text))

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()