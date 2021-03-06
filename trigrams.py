import io
import string
import random
import sys


def file_load(input_text):
    imported_file = io.open(input_text, mode='r')
    tokens = imported_file.read().replace('-', ' ').lower().split()
    new_tokens = [token.strip(string.punctuation) for token in tokens]
    return new_tokens


def make_dict(tokens):
    text_dict = {}
    i = 0
    while i < len(tokens) - 2:
        token_set = tokens[i:i+3]
        key = tuple(token_set[:2])
        value = token_set[-1:]
        if key in text_dict:
            text_dict[key].extend(value)
        else:
            text_dict[key] = value
        i += 1
    return text_dict


def build_output(text_dict, output_length):
    output_list = []
    first = random.sample(text_dict.keys(), 1).pop()
    output_list.extend(first)
    words = choose_next(first, text_dict)
    output_list.append(words[1])
    step = 3
    while step < output_length:
        words = choose_next(words, text_dict)
        output_list.append(words[1])
        step += 1
    print(output_list)
    new_file = open('output.txt', 'w')
    new_file.write(' '.join(output_list))
    return output_list


def choose_next(current_key, text_dict):
    current = text_dict[current_key]
    new_list = [current_key[0], current_key[1], random.choice(current)]
    new_tuple = tuple(new_list[-2:])
    return new_tuple


def main(source_file, num_runs):
    build_output(make_dict(file_load(source_file)), num_runs)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
