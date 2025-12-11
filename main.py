from stats import count_words, count_chars, sort_dict
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        report(sys.argv[1])

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
