debugToggle = False
def debug(text):
    if debugToggle:
        print(text)

def convertToHtml(inputFile):
    htmlLines = []

    with open(inputFile, "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        line = line.strip("\t")

    tags = ["-", "#-", "!--", "---"]
    fullLineTags = ["-", "#-", "!--", "---"]
    tagshtml = []
    htmlTags = []
    endTags = []
    tagNumber = 0

    tags, fullLineTags, tagshtml, htmlTags, endTags = readTagsFile("data/internal/tagsFile.txt")

    print(tags)
    print(fullLineTags)
    print(tagshtml)
    print(endTags)

    closeTag = "</div>"
   
    titleLine = lines[0]
    titleLine = titleLine.strip()
    if titleLine.startswith("!") and titleLine.startswith("!"):
        title = titleLine.strip("!")

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
        
        isEndTag = False
        for endtag in endTags:
            debug(f"endtag: {endtag}")
            debug(f"line: {line}")
            if line == endtag and stared:
                debug(f"yesssssssir")
                htmlLines.append(closeTag)
                isEndTag = True

        if isEndTag:
            isEndTag = False
            continue

        skip = False
        for tag in tags:
            debug(f"tag: {tag}")
            if "*" in tag:
                tagSplit = tag.split("*")
                debug(f"tagSplit: {tagSplit}")
                debug(f"lineS: {line.startswith(tagSplit[0])}\nlineE: {line.endswith(tagSplit[1])}")
                if line.startswith(tagSplit[0]) and line.endswith(tagSplit[1]):
                    htmlLines.append(closeTag)
                    inTextBlock = False
                    inHighlightBlock = True
                    debug("helllllll wpr;d")
                    filename = line.lstrip(f" {tagSplit[0]} ")
                    filename = filename.rstrip(f" {tagSplit[1]} ")
                    filename = filename.strip(" ")
                    tagNumber = tags.index(tag)
                    htmlLines.append(f'<div class="{tagshtml[tagNumber]}"><div class="filename">{filename}</div>')
                    stared = True
                    debug(f"filename: {filename}")
                    skip = True
                    continue
                continue
            
            if tag in line:
                debug(f"line: {line}")
                tagNumber = tags.index(tag)
                if tag in fullLineTags:
                    debug("I am Here")
                    if line != fullLineTags[fullLineTags.index(tag)]:
                        debug("I am Here2")
                        continue
                debug(f"tagNumber: {tagNumber}")
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

        
        if isTag or skip:
            #htmlLines.append("</div>")
            skip = False
            continue



        if inHighlightBlock or inTextBlock:
            try:
                print(htmlTags)
                print(tagNumber)
                print(f"<{htmlTags[tagNumber]}>{line}</{htmlTags[tagNumber]}><br>")
                htmlLines.append(f"<{htmlTags[tagNumber]}>{line}</{htmlTags[tagNumber]}><br>")
            except:
                htmlLines.append(f"{line}<br>")
        elif not inTextBlock:
            htmlLines.append(f'<div class="standardText"><p>')
            inTextBlock = True

    return "".join(htmlLines)

def readTagsFile(filename):
    with open(filename, 'r') as tagsFile:
        readlines = tagsFile.read().splitlines()

    Ttags = []
    TfullLineTags = []
    Ttagshtml = []
    ThtmlTags = []
    TendTags = []

    for x in range(len(readlines)):
        line = readlines[x]
        readlines[x] = line.split("|")
        Ttags.append(readlines[x][0])
        if readlines[x][1] == "1":
            TfullLineTags.append(readlines[x][0])

        Ttagshtml.append(readlines[x][2])
        ThtmlTags.append(readlines[x][3])
        if len(readlines[x]) > 4:
            TendTags.append(readlines[x][4])

    return Ttags, TfullLineTags, Ttagshtml, ThtmlTags, TendTags
