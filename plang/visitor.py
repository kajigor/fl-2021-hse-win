def main():
    sample = 1
    file = open('programs/program1.p', 'r')
    program = file.read().strip()
    file.close()


if __name__ == '__main__':
    # antlr4 -Dlanguage=Python3 -visitor plang.g4
    main()
