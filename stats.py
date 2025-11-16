def count_words(text):
    return len(text.strip().split())

def count_char(text):
    dict = {}
    for each in text:
        char = each.lower()

        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
        
    return dict

def sort_on(items):
    return items["num"]

def sorted_list(dict):
    result_list = [];
    for (key, value) in dict.items():
        if key.isalpha():
            result_list.append({"char": key, "num": value})

    result_list.sort(reverse=True, key=sort_on)

    return result_list