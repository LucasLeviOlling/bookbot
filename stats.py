def count_words(path):
    content = get_book_text(path)
    content = content.split()
    return len(content)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(path):
    text = get_book_text(path)
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_dict(dicti):
    dict_list = []
    for i in dicti:
        dict_list += [{"char": i, "num": dicti[i]}]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
