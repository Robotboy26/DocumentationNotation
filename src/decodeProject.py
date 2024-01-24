import os
import pdb
from readTagFile import readTagsFile

debugToggle = True
def debug(text):
    if debugToggle:
        print(text)

def decodeProject(inputFile):
    htmlLines = []
    shellCommands = []

    with open(inputFile, "r") as file:
        lines = file.read().splitlines()

    for line in lines:
        line = line.strip("\t")

    tags = ["-", "#-", "!--", "---"]
    fullLineTags = ["-", "#-", "!--", "---"]
    tagshtml = []
    htmlTags = []
    endTags = []
    tagNumber = None

    tags, fullLineTags, tagshtml, htmlTags, endTags = readTagsFile("data/internal/tagsFile.txt")

    titleLine = lines[0]
    titleLine = titleLine.strip()
    if titleLine.startswith("!") and titleLine.startswith("!"):
        title = titleLine.strip("!")
    else:
        title = "This is a title"

    if not os.path.exists(title):
        os.mkdir(title)

    inHighlightBlock = False
    inTextBlock = False
    stared = False
    inFile = False
    inFileName = None
    for line in lines:
        # pdb.set_trace()
        line = line.strip()
        if line.startswith("!") and line.endswith("!"):
            continue
        
        isEndTag = False
        for endtag in endTags:
            debug(f"endtag: {endtag}")
            debug(f"line: {line}")
            if line == endtag and stared:
                debug(f"yesssssssir")
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
                    inTextBlock = False
                    inHighlightBlock = True
                    debug("helllllll wpr;d")
                    filename = line.lstrip(f" {tagSplit[0]} ")
                    filename = filename.rstrip(f" {tagSplit[1]} ")
                    filename = filename.strip(" ")
                    print(f"!!!   Filename This is huge {filename}   !!!")
                    # create the file
                    if os.path.exists(f"{title}/{filename}"):
                        with open(f"{title}/{filename}", 'a') as F:
                            pass # append lines to file
                    elif not os.path.exists(f"{title}/{filename}"):
                        with open(f"{title}/{filename}", 'w') as F:
                            pass # new file to start writing files too
                    inFile = True
                    inFileName = filename
                    tagNumber = tags.index(tag)
                    stared = True
                    debug(f"filename: {filename}")
                    skip = True
                    continue
                continue
            
            if tag in line:
                debug(f"line: {line}")
                tagNumber = tags.index(tag)
                if tagNumber == 0: # save anything inside bash tags
                    shellCommands.append(line)
                if tag in fullLineTags:
                    debug("I am Here")
                    if line != fullLineTags[fullLineTags.index(tag)]:
                        debug("I am Here2")
                        continue
                debug(f"tagNumber: {tagNumber}")
                if inHighlightBlock:
                    inHighlightBlock = False
                    inFile = False
                else:
                    inTextBlock = False
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
            skip = False
            continue



        if inHighlightBlock or inTextBlock:
                if inFile:
                    with open(f"{title}/{inFileName}", 'a') as F:
                        F.write(line)
                        F.write("\n")
                debug(line)
        elif not inTextBlock:
            inTextBlock = True

    print(f"shellCommands: {shellCommands}")
    return "\n".join(shellCommands)
