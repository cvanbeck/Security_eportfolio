from inspectHeaders import inspectHeaders
from checkHash import checkHash
from stringExtraction import printStrings
import sys

path = sys.argv[1]
algorithm = sys.argv[2]

print("\nHASH: ", checkHash(path, algorithm), "\nALGORITHM: ", algorithm, "\n")
print(printStrings(path))
inspectHeaders(path)


