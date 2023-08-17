from  WFT import wft
import urllib
from urllib import request

notifiers = ["-", "--", "!-", "#-"]

def findfile(readlines, ofile):
    for x in range(len(readlines)):
        string = readlines[x]
        if string[:3] == "!--":
            out = []
            temp = []
            print(f"string: {string}")
            print(string[len(string) - 1:])
            if string[len(string) - 1:] == "-" and string != "!--":
                filename = string.strip("!-- -")
                print(f"string: {string}")
                print(f"filename: {filename}")
                try:
                    while readlines[x + 1] != "!--":
                        x += 1
                        temp.append(readlines[x])
                except:
                    pass
            print(f"x {x}")
            print(string)

            for x in range(len(temp)):
                if temp[x] != "---":
                    try:
                        out.append(temp[x])
                    except:
                        pass
            
            print(out)
            with open("t.tmp", 'w') as tempfile:
                tempfile.write("\n".join(out))

            wft("t.tmp", ofile, filename)

def findLines(lines):
    outlines = []
    inHighlightBlock = False
    for line in lines:
        if line == "-" and not inHighlightBlock or line == "#-" and not inHighlightBlock or line.startswith("!--") and not inHighlightBlock or line.startswith("---") and not inHighlightBlock:
            inHighlightBlock = True

        elif line == "-" and inHighlightBlock or line == "#-" and inHighlightBlock or line.startswith("!--") and inHighlightBlock or line.startswith("---") and inHighlightBlock:
            inHighlightBlock = False
        else:
            if inHighlightBlock:
                outlines.append(line)
            else:
                continue

    return "\n".join(outlines)


def downloadFromWeb(urlList, fileList):
    for url in urlList:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        with open(fileList[urlList.index(url)], "w") as outFile:
            outFile.write(text)

def main():
    out = []
    inputFile = input("type the filename to parse: ")
    ofile = input("type the file you want to output to or leave black for standard output: ")

    enableGithubFetch = True
    urlList = ['https://raw.githubusercontent.com/Robotboy26/myOSBlog/main/src/docs/part1.dn']
    fileList = ["part1.dn"]

    if enableGithubFetch:
        downloadFromWeb(urlList, fileList)
        inputFile = fileList[0]

    if inputFile == "":
        inputFile = "part1.dn"

    if ofile == "":
        ofile = "p.out"


    with open(inputFile, 'r') as inputFile:
        readlines = inputFile.read().splitlines()
    
    outputs = findLines(readlines)
    print(outputs)

    with open(ofile, 'w') as outfile:
        outfile.write(outputs)

    #findfile(readlines, ofile)

main()
