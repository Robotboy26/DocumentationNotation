from  WFT import wft

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

def main():
    out = []
    filename = input("type the filename to parse: ")
    ofile = input("type the file you want to output to or leave black for standard output: ")

    if ofile == "":
        ofile = "p.out"

    with open(filename, 'r') as inputFile:
        readlines = inputFile.read().splitlines()
    
    with open(ofile, 'w') as outfile:
        pass


    for x in range(len(readlines)):
        string = readlines[x]
        if string == "-":
            x += 1
            out = []
            temp = []
            print(string)
            while readlines[x] != "-":
                print(readlines[x])
                x += 1
                temp.append(readlines[x])
            print(f"x {x}")
            print(string)
            out = temp

            out = "\n".join(out)
            with open("p.out", 'a') as file:
                file.write(out)

            print(out)
    
    findfile(readlines, ofile)

main()
