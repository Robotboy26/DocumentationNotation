import re
import urllib.request
from lxml import etree, html

indent = "&nbsp;" * 4
tab = "\t"


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
    cssLines.append(f""".temp2class {{
            width: 100%;
            margin: 0 auto;
            color: black;
            text-align: left;
            font-size: {fontSize}px;
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
    cssLines.append(f""".filename {{
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


def convertToHtml(inputFile, backgroundColor, normalColor, fontSize, width, height):
    htmlLines = []
    htmlLines.append(f"""<html><head><title>Your Website Title</title><link rel="stylesheet" href="styles.css"></head><body>""")

    with open(inputFile, "r") as file:
        lines = file.readlines()

    inHighlightBlock = False
    bodyBlock = False
    for line in lines:
        if line == "":
            htmlLines.append('<br>')
            continue

        if line == "\n":
            htmlLines.append('<br>')
            continue

        if line.startswith("\t"): # need to fix
            htmlLines.append('\t')

        line = line.strip()
        if line.startswith("!") and line.endswith("!"):
            htmlLines.append('<div style="font-size: 32px; font-weight: bold; text-align: center;">')
            htmlLines.append(line.strip("!"))
            htmlLines.append('</div>')
            continue

        if line == "-" and not inHighlightBlock or line == "#-" and not inHighlightBlock or line.startswith("!--") and not inHighlightBlock or line.startswith("---") and not inHighlightBlock:
            inHighlightBlock = True
            htmlLines.append('</div>')
            htmlLines.append('<br>') # pretty sure i fixed now with .append('<br>')
            htmlLines.append(f'<div class="highlightedBlock"><p>')

        elif line == "-" and inHighlightBlock or line == "#-" and inHighlightBlock or line.startswith("!--") and inHighlightBlock or line.startswith("---") and inHighlightBlock:
            inHighlightBlock = False
            htmlLines.append('</p></div>')
            htmlLines.append('<br>') # pretty sure i fixed now with .append('<br>')
        else:
            if inHighlightBlock:
                htmlLine = f'{indent}{indent}{line}<br>' # htmlLine = f'{indent}{indent}<span style="font-family: monospace; color: white;">{line}</span><br>'
            else:
                if bodyBlock != True:
                    htmlLine = f'<div class="tempclass2">{line}'
                    bodyBlock = True
                else:
                    htmlLines.append('<br>')
                    htmlLine = f'{line}'
            htmlLines.append(htmlLine)
            #htmlLines.append("</body>\n</html>")

        #htmlLines.append("</h1>")

    return "".join(htmlLines)


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
    urlList = ['https://raw.githubusercontent.com/Robotboy26/myOSBlog/main/docs/test.dn']
    fileList = ["test.dn"]

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
        print(html)
        print("\n\n\n\n\n\n\n\n")
        prettyHtml = etree.tostring(html, encoding='unicode', pretty_print=True)
        print(prettyHtml)

    with open(outputFile, 'w') as htmlFile:
        htmlFile.write(prettyHtml)




