import sys

from pathlib import Path


def search(pattern, filepath):
    path_obj = Path(filepath)
    with path_obj.open() as file_:
        lines = file_.readlines()
        for line_number, line in enumerate(lines, 1):
            line = line.rstrip('\n')
            if pattern in line:
                print(line_number, line, sep='\t')

def main():
    args = sys.argv
    if len(args) > 1:
        pattern = args[1]
        search_path = args[2]
        search(pattern, search_path)
    else:
        error1 = "usage: grepper.py pattern search_path"
        error2 = "grepper.py: error: the following arguments are required: pattern, search_path"
        print(error1, error2, sep='\n')


if __name__ == '__main__':
    main()