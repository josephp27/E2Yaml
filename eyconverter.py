import re
from collections import Mapping

from utilities import ignored_term_in_line, process_key, convert_key_value_pairs_to_dictionary


class EyConverter:

    def __init__(self):
        self.special_characters = re.compile('[@!#$%^&*()<>?\|}{~]')

        self.lines = []
        self.ignored_terms = set()
        self.preserved_words_dict = {}
        self.d = {}
        self.output = []

    def load_file(self, filename):
        with open(filename) as file:
            self.lines = file.readlines()

        return self

    def ignore_lines_containing(self, *args):

        self.ignored_terms = set(args)

        return self

    def preserve_words(self, *args):

        for word in args:
            self.preserved_words_dict[word.lower()] = word

        return self

    def convert_to_dictionary(self):

        for line in self.lines:

            if ignored_term_in_line(self.lines, self.ignored_terms):
                continue

            key, value = line.split(':', 1)

            processed_key = process_key(key, self.preserved_words_dict)
            processed_value = value.strip()

            self.d = convert_key_value_pairs_to_dictionary(processed_key, processed_value, self.d)

        return self

    def build_output(self, yml_dict, tab_count):
        for key, value in yml_dict.items():
            self.output.append('\t' * tab_count + key + ':')

            if isinstance(value, Mapping):
                self.build_output(value, tab_count + 1)
            else:
                if self.special_characters.search(value):
                    value = f'"{value}"'

                self.output[-1] += f' {value}'

    def show(self):

        self.build_output(self.d, 0)
        for line in self.output:
            print(line)

    def write_file(self, filename):

        self.build_output(self.d, 0)
        with open(filename, 'w+') as file:
            for line in self.output:
                file.write(f'{line}\n')
