from mchecksum import genGetFile, getCheckFromGetFile

genGetFile("data/internal/getFile.txt")
files, md5s, sha256s = getCheckFromGetFile("data/internal/getFile.txt")

print(files)
print(md5s)
print(sha256s)
