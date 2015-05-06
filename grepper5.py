import argparse

from pathlib import Path


def search(pattern, filepath, **flags):
    path_obj = Path(filepath)
    with path_obj.open() as file_:
        lines = file_.readlines()
        for line_number, line in enumerate(lines, 1):
            line = line.rstrip('\n')
            if pattern in line:
                print(line_number, line, sep='\t')

def main():
    parser = argparse.ArgumentParser(description='Simplistic search program.')

    parser.add_argument('pattern', action='store')
    parser.add_argument('search_path', action='store')

    args = parser.parse_args()  # returns a Namespace object
    search(args.pattern, args.search_path)

if __name__ == '__main__':
    main()