filename = "css.txt"

with open(filename, "r") as file:
    readlines = file.read().splitlines()


out = []
for line in readlines:
    out.append(f"{line}\n")
    content = "".join(out)

with open("cssout.txt", 'w') as cssOut:
    cssOut.write(content)
