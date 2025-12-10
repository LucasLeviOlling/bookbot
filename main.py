from stats import count_words, count_chars, sort_dict
def main():
    path = "books/frankenstein.txt"
    report(path)

def report(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(path)} total words")
    print("--------- Character Count -------")
    chars = count_chars(path)
    sorted_chars = sort_dict(chars)
    for i in range(len(sorted_chars)):
        if sorted_chars[i]["char"].isalpha():
            print(f"{sorted_chars[i]["char"]}: {sorted_chars[i]["num"]}")
        else:
            continue

if __name__ == "__main__":
    main()    
