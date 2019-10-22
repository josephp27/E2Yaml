import re
from collections import Mapping

from utilities import read_from_clipboard, write_to_clipboard, ignored_term_in_line, \
    convert_key_value_pairs_to_dictionary, process_key


class EyConverter:

    def __init__(self, log=False, separate=False):

        self.special_characters = re.compile('[@!#$%^&*()<>?\|}{~]')
        self.lines = []
        self.ignored_terms = set()
        self.preserved_words_dict = {}
        self.d = {}
        self.output = []
        self.log = log
        self.separate = separate
        
    def add_line(self, line):
        
        self.lines.append(line)
        return self

    def from_clipboard(self):

        self.lines = filter(None, read_from_clipboard().split('\n'))
        return self

    def to_clipboard(self):

        self.build_output(self.d, 0, 0)
        write_to_clipboard('\n'.join(str(line) for line in self.output))

    def load_file(self, filename):

        with open(filename) as file:
            self.lines = filter(lambda x: x != '\n', file.readlines())
            print(self.lines)

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

            line.strip()

            self.print(f"PARSING: \t{line}", new_line=False)

            if ignored_term_in_line(line, self.ignored_terms):
                self.print("\tSKIPPING")
                continue

            key, value = line.split(':', 1)

            processed_key = process_key(key, self.preserved_words_dict)
            processed_value = value.strip()

            self.d = convert_key_value_pairs_to_dictionary(processed_key, processed_value, self.d)

            self.print("\tOK")

        return self

    def build_output(self, yml_dict, tab_count, level):

        index = 0
        for key, value in yml_dict.items():

            if level == 0 and self.separate and index != 0:
                self.output.append('')

            index += 1
            
            self.output.append('  ' * tab_count + key + ':')

            if isinstance(value, Mapping):
                self.build_output(value, tab_count + 1, level + 1)
            else:
                if self.special_characters.search(value):
                    value = f'"{value}"'

                self.output[-1] += f' {value}'

    def show(self):

        self.build_output(self.d, 0, 0)
        for line in self.output:
            print(line)

    def write_file(self, filename):

        self.build_output(self.d, 0, 0)
        with open(filename, 'wb+') as file:
            for line in self.output:
                file.write(str.encode(line + "\n"))

    def print(self, message, new_line=True):
        if self.log:
            print(message.rstrip(), end='\n' if new_line else '')


def load_file(filename, log=False, separate=False):
    return EyConverter(log, separate).load_file(filename)


def from_clipboard(log=False, separate=False):
    return EyConverter(log, separate).from_clipboard()
