def ignored_term_in_line(line, ignored_terms):

    for word in line:
        print(word)
        if word in ignored_terms:
            return True

    return False


def process_key(key, preserved_words_dict):
    key = key.strip().lower()
    key = replace_separator_in_preserved_words(key, preserved_words_dict)
    tree = key.split('_')
    converted_cases = convert_casing(tree, preserved_words_dict)

    return convert_separator_back(converted_cases)


def convert_casing(targets, source):
    for i, word in enumerate(targets):
        targets[i] = source.get(word, word)

    return targets


def replace_separator_in_preserved_words(target, preserved_words):
    for key, val in preserved_words.items():
        modified_val = val.replace('_', '|')

        target = target.replace(val, modified_val)

    return target


def convert_separator_back(targets):
    for i, word in enumerate(targets):
        targets[i] = word.replace('|', '_')

    return targets


def convert_key_value_pairs_to_dictionary(keys, value, dictionary):

    level = dictionary
    for i in range(len(keys) - 1):
        node = keys[i]

        if node in level:
            level = level[node]
        else:
            level[node] = {}
            level = level[node]

    level[keys[-1]] = value

    return dictionary
