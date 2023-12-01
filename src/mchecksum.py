import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import sys

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def selectFolder():
    root = tk.Tk()
    root.withdraw()
    
    folderPath = filedialog.askdirectory(title="Select a Folder")
    
    if folderPath:
        print(f"Selected folder: {folderPath}")
    else:
        print("No folder selected.")

    return folderPath

def getFilesInFolder(folderPath):
    fileList = []
    for root, dirs, files in os.walk(folderPath):
        for file in files:
            filePath = os.path.join(root, file)
            fileList.append(filePath)
    return fileList

def mchecksums(files):
    md5s = []
    sha256s = []
    for filePath in files:
        md5s.append(calculate_md5(filePath))
        sha256s.append(calculate_sha256(filePath))

    return md5s, sha256s

def genCheckFile(files, md5s, sha256s, filename):
    with open(filename, 'w') as temp: # if the file is not created yet
        temp.close()

    with open(filename, 'a') as checkfile: # now use the real file
        if len(md5s) == 1 and len(sha256s) == 1 and len(files) == 1:
            changedFilename = os.path.basename(files)
            checkfile.write(f"{changedFilename}|{md5s}|{sha256s}\n")
        else:
            for x in range(len(files)):
                changedFilename = os.path.basename(files[x])
                checkfile.write(f"{changedFilename}|{md5s[x]}|{sha256s[x]}\n")

def genGetFile(filename, basePath="https://raw.githubusercontent.com/Robotboy26/DNDocs/main/docs/"):
    files = getFilesInFolder("data/text")
    md5s, sha256s = mchecksums(files)
    urlList = []
    for file in files:
        urlList.append(f"{basePath}{file}")
    getFileData = []
    for x in range(len(urlList)):
        url = urlList[x]
        md5 = md5s[x]
        sha256 = sha256s[x]
        if x == 0:
            getFileData.append(f"{basePath}\n")
        else:
            getFileData.append(f"{url}|{md5}|{sha256}\n")

    with open(filename, "w") as getFile:
        getFile.write("".join(getFileData))

def strFromEnd(string, basePath):
    x = len(basePath) - len(string)
    return string[x:]
    

def getCheckFromGetFile(filename):
    with open(filename, "r") as f:
        readlines = f.read().splitlines()

        basePath = readlines[0]
        print(basePath)
            
        lines = []
        for line in readlines:
            lines.append(line.split("|"))
        
        filePaths = []
        md5s = []
        sha256s = []

        for x in range(len(lines) - 1):
            filePaths.append(strFromEnd(lines[x + 1][0], basePath))
            md5s.append(lines[x + 1][1])
            sha256s.append(lines[x + 1][2])

        return filePaths, md5s, sha256s



    with open("data/internal/getFile.txt", "w") as f:
        f.write("".join(getFileData))

    print("wrote getFile")

def main():
    checkFilename = "data/checksums.txt"
    if len(sys.argv) > 1:
        folderPath = sys.argv[1]
    else:
        folderPath = selectFolder()
    files = getFilesInFolder(folderPath)
    md5s, sha256s = mchecksums(files)
    genCheckFile(files, md5s, sha256s, checkFilename)


if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")

    main()
