files = "/home/bycho/Projects/gitHub/hello-world/Python/study/file/score.txt"
score_file = open(files, "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
print()
score_file.close()