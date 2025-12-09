import hashlib
import os
from datetime import datetime

def fileToSHA256(filePath):
    with open(filePath, "rb") as f:
        bytes = f.read()
        f.close()
        readableHash = hashlib.sha256(bytes).hexdigest()
        print(readableHash)
        return readableHash
    
def appendToCsv(destination, content):
    with open(f"{destination}.csv", "a") as f:
        f.write(content +"\n")
        f.close()
        return

def clearCsv(filePath):
    with open(f"{filePath}.csv", "w") as f:
        f.write("")
        f.close()

def main(destination):
    clearCsv(destination)
    appendToCsv(destination, "Date and Time,SHA256_Hash,Filename")
    numberOfFiles = 0
    folderRoot = "folder"
    for path, folders, files in os.walk(f"{folderRoot}"):
        for file in files:
            readableHash = fileToSHA256(f"{folderRoot}/{file}")
            fileName = os.path.basename(file)
            date = datetime.now()
            content = f"\"{date}\",{readableHash},\"{fileName}\""
            appendToCsv(destination, content)
            numberOfFiles += 1
    print(f"{numberOfFiles} files converted to SHA256 and appendd to {destination}.csv")

main("storedHash")
with open("folder\Screenshot 2024-11-05 112444.png", "a") as f:
    f.write("103210")

with open("folder\Screenshot 2024-11-16 014527.png", "a") as f:
    f.write("103210")
main("secondStoredHash")
