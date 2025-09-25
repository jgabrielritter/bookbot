def get_num_words(text):
    """
    Count the number of words in the given text.
    Splits the text on whitespace and returns the length.
    """
    words = text.split()
    return len(words)


def get_char_counts(text):
    """
    Count the number of times each character appears in the text.
    Converts characters to lowercase to avoid duplicates.
    Returns a dictionary: {character: count}
    """
    chars = {}
    for c in text.lower():  # convert each character to lowercase
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_char_counts(char_counts):
    """
    Convert the char_counts dict into a sorted list of dicts.
    Each dict looks like: {"char": <char>, "num": <count>}
    Sorted from greatest to least by "num".
    """
    # convert dict to list of {"char": c, "num": n}
    sorted_list = [{"char": c, "num": n} for c, n in char_counts.items()]

    # sort in place by "num", descending
    sorted_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_list
