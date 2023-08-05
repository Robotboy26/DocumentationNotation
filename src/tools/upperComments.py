upper = True
comments = [";", "#"]


def main():
    filename = input("Type the target filename: ")
    
    formatting = input("Type 1 for upper and 0 for lower: ")

    if formatting == "1":
        upper = True
    elif formatting == "0":
        upper = False
    else:
        quit("that was not one of the options")

    with open(filename, 'r') as file:
        read = file.read().splitlines()

    read = "\n".join(read)
    read = list(read)
    for x in range(len(read)):
        if read[x] in comments:
            x += 1
            while read[x] == " ":
                x += 1
            if upper == True:
                print(read[x])
                print(f"x: {x}")
                read[x] = read[x].upper()
            else:
                read[x] = read[x].lower()


    with open("o.out", "w") as file:
        file.write("".join(read))



main()
