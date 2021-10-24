import sys


def main():
    if len(sys.argv) != 2:
        print("Need 1 argument: name of input file")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.replace(" ", "")
        if line.startswith("trans"):
            trans = line[line.find('[') + 1: line.find(']')].split(',')
            line = "trans=[" + ','.join(set(trans)) + "]\n"
        line = line.replace(",", ", ")
        line = line.replace("=", " = ")
        lines[i] = line
    lines = [line for line in lines if not line == '\n']
    with open(sys.argv[1], 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    main()
