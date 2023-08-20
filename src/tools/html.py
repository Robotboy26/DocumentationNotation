import re
import urllib.request
from lxml import etree, html

tab = "\t"

def convertToHtml(inputFile, backgroundColor, normalColor, fontSize, width, height):
    htmlLines = []

    with open(inputFile, "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        line = line.strip("\t")

    tags = ["-", "#-", "!--", "---"]
    fullLineTags = ["-", "#-", "!--", "---"]
    tagshtml = []

    tags, fullLineTags, tagshtml = readTagsFile("tagsFile.txt")

    print(tags)
    print(fullLineTags)
    print(tagshtml)

    closeTag = "</div>"
    
    Tline = lines[0]
    Tline = Tline.strip()
    if Tline.startswith("!") and Tline.startswith("!"):
        title = Tline.strip("!")

    print(title)
    #title = "This is a title"

    htmlLines.append(f"""<html><head><title>{title}</title><link rel="stylesheet" href="styles.css"></head><body>""")

    inHighlightBlock = False
    inTextBlock = False
    stared = False
    for line in lines:
        line = line.strip()
        if line.startswith("!") and line.endswith("!"):
            htmlLines.append('<div style="font-size: 32px; font-weight: bold; text-align: center;">') # open tag
            htmlLines.append(line.strip("!")) # write title
            htmlLines.append(closeTag) # close tag
            continue

        if line == "---" and stared:
            htmlLines.append(closeTag)
            continue

        for tag in tags:
            print(f"tag: {tag}")
            if "*" in tag:
                tagSplit = tag.split("*")
                #print(f"tagSplit: {tagSplit}")
                print(f"lineS: {line.startswith(tagSplit[0])}\nlineE: {line.endswith(tagSplit[1])}")
                if line.startswith(tagSplit[0]) and line.endswith(tagSplit[1]):
                    htmlLines.append(closeTag)
                    inTextBlock = False
                    inHighlightBlock = True
                    print("helllllll wpr;d")
                    filename = line.strip("-")
                    filename = filename.strip(" ")
                    htmlLines.append(f'<div class="{tagshtml[tagNumber]}"><div class="filename">{filename}</div>')
                    stared = True
                    print(filename)
                    continue
                continue

            if tag in line:
                print(f"line: {line}")
                tagNumber = tags.index(tag)
                if tag in fullLineTags:
                    #print("I am Here")
                    if line != fullLineTags[fullLineTags.index(tag)]:
                        #print("I am Here2")
                        continue
                print(f"tagNumber: {tagNumber}")
                if inHighlightBlock:
                    htmlLines.append(closeTag)
                    inHighlightBlock = False
                else:
                    htmlLines.append(closeTag)
                    inTextBlock = False
                    htmlLines.append(f'<div class="{tagshtml[tagNumber]}">')
                    inHighlightBlock = True
        
        isTag = False
        for tag in tags:
            if tag in line:
                if tag in fullLineTags:
                    if line == fullLineTags[fullLineTags.index(tag)]:
                        isTag = True
            if "*" in tag:
                if line.startswith(tagSplit[0]) and line.endswith(tagSplit[1]):
                    istTag = True

        
        if isTag:
            #htmlLines.append("</div>")
            continue



        if inHighlightBlock:
            htmlLines.append(f"{line}<br>")
        elif not inTextBlock:
            htmlLines.append(f'<div class="standardText"><p>')
            inTextBlock = True

        if inTextBlock:
            htmlLines.append(f"{line}<br>")

    return "".join(htmlLines)

def readTagsFile(filename):
    with open(filename, 'r') as tagsFile:
        readlines = tagsFile.read().splitlines()

    Ttags = []
    TfullLineTags = []
    Ttagshtml = []

    for x in range(len(readlines)):
        line = readlines[x]
        readlines[x] = line.split("|")
        Ttags.append(readlines[x][0])
        if readlines[x][1] == "1":
            TfullLineTags.append(readlines[x][0])

        Ttagshtml.append(readlines[x][2])

    return Ttags, TfullLineTags, Ttagshtml

def generateStyles(inputFile, backgroundColor, normalColor, fontSize, width, height):
    cssLines = []
    # css body
    print(f"{inputFile}, {backgroundColor}, {normalColor}, {fontSize}, {width}, {height}")
    cssLines.append(f"""body {{
            font-family: Arial, sans-serif;
            font-size: {fontSize}px;
            width: {width}%;
            background-color: #FFD0A0;
            margin: 0 auto;
            padding: 0 auto;
            text-align: left;
            }}\n""")
    cssLines.append(f""".header {{
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
            }}\n""")
    cssLines.append(f""".highlightedBlock {{
            background-color: {backgroundColor};
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")
    cssLines.append(f""".commentBlock {{
            background-color: #32631f;
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")
    cssLines.append(f""".testBlock {{
            background-color: #2d1769;
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")
    cssLines.append(f""".standardText {{
            font-family: Arial, sans-serif;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            background-color: #FFD0A0;
            margin: 0 auto;
            padding: 0 auto;
            text-align: left;
            }}\n""")
    cssLines.append(f""".filename {{ 
            background-color: #f705af;
            position:relative;
            left: 42%;
            width: 16%;
            text-align: center;
            border-radius: 4px;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
            }}\n""")
    cssLines.append(f""".highlighted-text {{
            margin-top: 20px;
            }}\n""")
    cssLines.append(f""".copy-button {{
            display: block;
            margin-top: 10px;
            padding: 8px 16px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            }}\n""")
    cssLines.append(f""".copy-button:hover {{
            background-color: #555;
            }}\n""")
    cssLines.append(f""".tempclass {{
            background-color: {backgroundColor};
            border-radius: 8px;
            padding: 12px;
            line-height: 1.5;
            font-size: {fontSize}px;
            width: 100%; # 100% because it is 100% of the bodys width
            margin: 0 auto;
            text-align: left;
            color: {normalColor};
            }}\n""")           

    return "".join(cssLines)

def downloadFromWeb(urlList, fileList):
    for url in urlList:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        with open(fileList[urlList.index(url)], "w") as outFile:
            outFile.write(text)
    

if __name__ == "__main__":
    inputFile = "input.txt"
    inputStyle = ""
    outputFile = "output.html"
    backgroundColor = "#28289C"
    normalColor = "FFD0A0" #F3F3F3 Backup Option
    fontSize = 14
    width = 65
    height = 0 # not used right now

    enableGithubFetch = False
    urlList = ['https://raw.githubusercontent.com/Robotboy26/myOSBlog/main/src/docs/test.dn']
    fileList = ["part1.dn"]

    if enableGithubFetch:
        downloadFromWeb(urlList, fileList)
        inputFile = fileList[0]

    cssContent = generateStyles(inputFile, backgroundColor, normalColor, fontSize, width, height)
    htmlContent = convertToHtml(inputFile, backgroundColor, normalColor, fontSize, width, height)

    with open("styles.css", 'w') as styleFile:
        styleFile.write(cssContent)

    with open("notPretty.html", 'w') as rawHtmlFile:
        rawHtmlFile.write(htmlContent)

    print(f"CSS file 'styles.css' generated.")
    print(f"HTML file '{outputFile}' generated.")

    # make html pretty
    with open("notPretty.html", 'r') as notPretty:
        html = html.fromstring("".join(notPretty.read().splitlines()))
        #print(html)
        #print("\n\n\n\n\n\n\n\n")
        prettyHtml = etree.tostring(html, encoding='unicode', pretty_print=True)
        #print(prettyHtml)

    with open(outputFile, 'w') as htmlFile:
        htmlFile.write(prettyHtml)




