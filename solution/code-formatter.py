import sys


def main():
    if len(sys.argv) != 2:
        print("Need 1 argument: name of input file")
        sys.exit(1)
    lines = open(sys.argv[1], 'r').readlines()
    line = lines[4]
    ind1 = line.find('[')
    ind2 = line.find(']')
    trans = line[ind1 + 1: ind2].split(',')
    lines[-1] = "trans=[" + ','.join(set(trans)) + "]\n"
    open(sys.argv[1], 'w').writelines(lines)


if __name__ == '__main__':
    main()
