from ie_utils import tokenize

import sys

def main():
    for word in sys.argv:
        print(tokenize(word))

if __name__ == "__main__":
    main()