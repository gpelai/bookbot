from stats import get_num_words, get_num_letters, dict_to_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    file_text = get_book_text(file_path)
    dict_letters = get_num_letters(file_text)
    word_count = get_num_words(file_text)

    msg = f"""============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    print(msg)
    dict_to_list(dict_letters)

main()