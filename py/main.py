import sys

# {{ RUN_IMPORT }}

if __name__ == '__main__':
    if len(sys.argv[1:]) != 1:
        sys.exit(1)
    if Run(ProcessInput(sys.argv[1])):
        sys.exit(0)
    else:
        sys.exit(1)
