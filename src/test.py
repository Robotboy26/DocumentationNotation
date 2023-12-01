from conHtml import convertToHtml
import sys

if len(sys.argv) < 2:
    print("you did not set a input file using default")
    inputFile = "data/text/test.dn"
else:
    inputFile = sys.argv[1]

htmlContent = convertToHtml(inputFile)

with open("data/html/ThisIsATest.html", 'w') as testFile:
    testFile.write(htmlContent)

print(f"HTML file 'ThisIsATest' generated.")
print(htmlContent)
