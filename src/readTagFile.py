# format
# <tag>|<fullLineTag True/False 0/1>|<className>|<endTag (if there is none than the tag is the same to start and end)>
# example
# -|1|highlightedBlock
# "-" is the start and stop of the tag
# the full line has to be "-" to start/end the tag
# "highlightedBlock" is the class that is used for that tag
 

def readTagsFile(filename):
    with open(filename, 'r') as tagsFile:
        lines = tagsFile.read().splitlines()

    tags = []
    fullLineTags = []
    cssClass = []
    htmlTags = []
    endTags = []

    for line in lines:
        split = line.split("|")
        tags.append(split[0])
        if split[1] == "1":
            fullLineTags.append(split[0])
        cssClass.append(split[2])
        htmlTags.append(split[3])
        if len(split) > 4: # if has sperate end tag
            endTags.append(split[4])

    return tags, fullLineTags, cssClass, htmlTags, endTags
