def main():
   book_path = "books/frankenstein.txt"
   text = get_text(book_path)
   num_words = word_count(text)
   print(f"{num_words} words found in the document")

def word_count(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()