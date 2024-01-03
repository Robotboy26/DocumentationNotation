import os
import sys
import urllib.request
from lxml import etree, html

from decodeProject import decodeProject

def fileFromUrl(url, urlBase):
    x = len(basePath) - len(string)
    return string[x:]

def getFileNames(urlList, urlBase):
    fileList = []
    for url in urlList:
        fileList.append(fileFromUrl(url, urlBase))

    return fileList

def downloadFromWeb(urlList, fileList):
    downloadedFiles, downloadedUrls = [], []
    for url in urlList:
        try:
            filename = fileList[urlList.index(url)]
            try:
                print(f"Downloading File '{filename}'")
                response = urllib.request.urlopen(url)
                data = response.read()
                text = data.decode('utf-8')
                with open(f"data/text/{filename}", "w") as outFile:
                    outFile.write(text)
                
                downloadedUrls.append(url)
                downloadedFiles.append(filename)
            except Exception as e:
                print(f"failed to download file {filename}, {e}")
        except Exception as e:
            print(f"failed to download a file, {e}")

    return downloadedFiles

def readGetFile(filePath):
    with open(filePath, "r") as getFile:
        getList, urlList = [], []
        get = getFile.read().splitlines()
        for line in get:
            getList.append(line.split("|"))

        for x in range(len(getList)):
            if x != 0:
                urlList.append(getList[x][0])
            else:
                urlBase = getList[x]

    cryptList = None
    return urlList, urlBase, cryptList

def main():

    useCloud = os.environ.get('USECLOUD')
    useFullRepo = os.environ.get('USEFULLREPO')
    checksumFile = os.environ.get('CHECKSUMFILE')
    getFile =  os.environ.get('GETFILE')

    inputStyle = ""
    outputFile = "output.html"
    backgroundColor = "#28289C"
    normalColor = "FFD0A0" #F3F3F3 Backup Option
    fontSize = 14
    width = 65
    height = 0 # not used right now

    urlList, urlBase, cryptList = readGetFile("data/internal/getFile.txt")
    print(urlList)

    # get the files names from the list of urls
    fileList = []
    for url in urlList:
        print(url)
        file = os.path.basename(url)
        fileList.append(file)

    print(f"fileList: {fileList}")

    if len(sys.argv) > 1:
        inputFile = sys.argv[1]
        print(f"CSS file 'styles.css' generated.")
        htmlContent = decodeProject(inputFile)
        outputFile = f'{inputFile.rstrip("dn")}html'
        with open(outputFile, 'w') as rawHtmlFile:
            rawHtmlFile.write(htmlContent)

        print(f"HTML file '{outputFile}' generated.")
    else:
        quit("you did not set a input file this has no support for defaults")

if __name__ == "__main__":
    main()
