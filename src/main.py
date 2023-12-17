import os
import sys
import urllib.request
from lxml import etree, html

from styles import generateStyle
from conHtml import convertToHtml

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

    if not os.path.exists("data/text") or not os.path.exists("data/text") or not os.path.exists("data/internal"):
        os.makedirs("data/text")
        os.makedirs("data/html")
        os.makedirs("data/internal")

    inputStyle = ""
    outputFile = "output.html"
    backgroundColor = "#28289C"
    normalColor = "FFD0A0" #F3F3F3 Backup Option
    fontSize = 14
    width = 65
    height = 0 # not used right now

    enableGithubFetch = False
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
        cssContent = generateStyle(backgroundColor, normalColor, fontSize, width, height)
        with open("data/html/styles.css", 'w') as styleFile:
            styleFile.write(cssContent)
        print(f"CSS file 'styles.css' generated.")
        htmlContent = convertToHtml(inputFile)
        outputFile = f'{inputFile.rstrip("dn")}html'
        with open(outputFile, 'w') as rawHtmlFile:
            rawHtmlFile.write(htmlContent)

        print(f"HTML file '{outputFile}' generated.")
    else:
        print("you did not set a input file using default")
        inputFile = "../sampleText/part1.dn"

    downloadedFiles = downloadFromWeb(urlList, fileList)

    cssContent = generateStyle(backgroundColor, normalColor, fontSize, width, height)
    with open("data/html/styles.css", 'w') as styleFile:
        styleFile.write(cssContent)
    print(f"CSS file 'styles.css' generated.")
    
    for inputFile in downloadedFiles:
        inputFileSource = f"data/text/{inputFile}"
        htmlContent = convertToHtml(inputFileSource)
        
        outputFile = f'{inputFile.rstrip("dn")}html'
        with open(f"data/html/{outputFile}", 'w') as rawHtmlFile:
            rawHtmlFile.write(htmlContent)

        print(f"HTML file '{outputFile}' generated.")

    #with open("notPretty.html", 'r') as notPretty:
    #    html = html.fromstring("".join(notPretty.read().splitlines()))
    #    prettyHtml = etree.tostring(html, encoding='unicode', pretty_print=True)

    #with open(outputFile, 'w') as htmlFile:
        #htmlFile.write(prettyHtml)





if __name__ == "__main__":
    main()
