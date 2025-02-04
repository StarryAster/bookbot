def book_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    words = file_contents.split()
    i = 0
    for word in words:
        i += 1
    return i

def char_count(file_contents):
    lc_book = file_contents.lower()
    letter_count = {}
    i = 0
    while i < len(lc_book):
        if lc_book[i] in letter_count:
            letter_count[lc_book[i]] += 1
        else:
            letter_count[lc_book[i]] = 1
        i += 1
    return letter_count

def reverse_dict(dict):
    reverse = {}
    for item in dict:
        reverse[dict[item]] = item
    return reverse

def was_found(dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book_words())} words were found in the document")
    dict = reverse_dict(dict)
    dict_tuples = sorted(dict.items(), reverse=True)
    new_dict = {}
    for i in range (len(dict_tuples)):
        new_dict[dict_tuples[i][0]] = dict_tuples[i][1]
    new_dict = reverse_dict(new_dict)
    for entry in new_dict:
        if entry.isalpha() == True:
            print(f"The '{entry}' character was found {new_dict[entry]} times")
    print("--- End report ---")

letters = char_count(book_words())
was_found(letters)