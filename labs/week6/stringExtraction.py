import re
import sys

def extract_strings(path):
    with open(path, "rb") as f:
        data = f.read()
    pattern = rb"[ -~]{4,}"
    return re.findall(pattern, data)


def printStrings(path):
    strings = extract_strings(path)

    for s in strings[:20]:
        print(s.decode(errors="ignore"))


if __name__ == "__main__":
    printStrings(sys.argv[1])
# This code extracts any human readable text from given filepath on command line