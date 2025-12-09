import hashlib
import sys

def checkHash(path, algorithm):
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


if __name__ == "__main__":
    print(checkHash(sys.argv[1], sys.argv[2]))