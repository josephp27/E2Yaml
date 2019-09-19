from collections import Mapping
import re

regex = re.compile('[@!#$%^&*()<>?\|}{~]')


def build_file(dict):
    output = []

    def build_lines(dict, tab_count):
        for k, v in dict.items():
            output.append('\t' * tab_count + k + ':')

            if isinstance(v, Mapping):
                build_lines(v, tab_count + 1)
            else:
                if regex.search(v) is None:
                    output[-1] += f' {v}'
                else:
                    output[-1] += f' "{v}"'

    build_lines(dict, 0)

    with open('outty.yml', 'w+') as file:
        for line in output:
            file.write(f'{line}\n')


with open('test.env') as file:
    lines = file.readlines()

d = {}
for line in lines:

    if 'CONVEYOR' in line or 'JAVA_OPTS' in line:
        continue

    key, value = line.strip().split(':', 1)
    value = value.strip()
    tree = key.lower().split('_')

    level = d
    for i in range(len(tree) - 1):
        node = tree[i]

        if node in level:
            level = level[node]
        else:
            level[node] = {}
            level = level[node]

    level[tree[-1]] = value

build_file(d)
