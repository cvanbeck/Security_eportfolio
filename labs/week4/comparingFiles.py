import pandas as pd

'''rehash the file, compare hashes and find alteration. If alteration found return which file was changed and when'''

def compareHashes():
    "reHash same folder"
    original = pd.read_csv("storedHash.csv")
    recent = pd.read_csv("secondStoredHash.csv")
    print(original.compare(recent))


compareHashes()