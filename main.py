def main():
    path = ("books/frankenstein.txt")
    #path = "\\\\wsl.localhost\\Ubuntu-20.04\\home\\klr6of8\\workspace\\github.com\\klr6of8\\bookbot\\books\\frankenstein.txt"
    text = get_book_text(path)
    print(text)
    total_words = count_words(text)
    totals = count_characters(text)
    my_list = []
    for alphabet in totals:
        if alphabet.isalpha():
            my_list.append({"letter": alphabet, "number": totals[alphabet]})
    my_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    for element in my_list:
        print(f"The '{element["letter"]}' character was found {element["number"]}")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def count_words(text):
    words = text.split()
    total = len(words)
    return total

def count_characters(text):
    totals = {}
    for letters in text:
        letter = letters.lower()
        if letter not in totals.keys():
            totals[letter] = 1
        else:
            totals[letter] += 1
    return totals

def sort_on(dict):
    return dict["number"]




main()
