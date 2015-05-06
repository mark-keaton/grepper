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
    pattern = args[1]
    search_path = args[2]
    search(pattern, search_path)

if __name__ == '__main__':
    main()