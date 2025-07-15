def get_num_words(contents):
    words = contents.split()
    return len(words)


def get_character_counts(content):
    char_count = {}

    content_lower = content.lower()

    for char in content_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_character_counts(char_count):
    sorted_list = [{"char": char, "num": count} for char, count in char_count.items()]

    sorted_list.sort(key=lambda x: x['num'], reverse=True)

    return sorted_list

