def get_book_text(filepath):
    with open(str(filepath)) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(filepath):
    book_text = get_book_text(filepath)
    word_count = len(book_text.split())
    return word_count

def get_letter_count(filepath):
    book_text = get_book_text(filepath).lower()
    letters = set(book_text)
    letter_counts = []

    for letter in letters:
        if (letter.isalpha()):
            letter_counts.append({"letter" : letter,
            "count": book_text.count(letter)})

    def sort_on(letter_count):
        return letter_count["count"]

    letter_counts.sort(reverse=True, key=sort_on)

    return letter_counts