def wft(filename=None, afile=None, tfile=None):
    if filename == None:
        filename = input("type the filename: ")
    if afile == None:
        afile = input("type the file that you want to append the output too or leave blank for create an output file: ")
    if tfile == None:
        tfile = input("type the file you want output to be writen to: ")

    if afile != "":
        appendFile = True


    with open(filename, 'r') as file:
        readlines = file.read().splitlines()
    
    if appendFile != True:
        outFile = "o.out"
        with open(outFile, "w") as out:
            out.write("")
    else:
        outFile = afile 

    with open(outFile, 'a') as out:
        for x in range(len(readlines)):
            readlines[x] = f"""echo "{readlines[x]}" >> {tfile}"""

        write = "\n".join(readlines)
        write = f"{write}\n"
        print(write)
        out.write(write)

if __name__ == "__main__":
    wft()
