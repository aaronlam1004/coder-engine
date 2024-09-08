import sys

# {{ RUN_IMPORT }}

if __name__ == '__main__':
    if len(sys.argv[1:]) != 1:
        sys.exit(1)
    print(Run(ProcessInput(sys.argv[1])))
