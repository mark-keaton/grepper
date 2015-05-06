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
    search('Superman', 'dc_heroes.txt')

if __name__ == '__main__':
    main()