import sys
import json


def load_data(filepath):
    data = ''
    with open(filepath, 'r') as infile:
        data = infile.read()
    return json.loads(data)


def pretty_print_json(data):
    return json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    filepath = sys.argv[1]
    print(pretty_print_json(load_data(filepath)))
