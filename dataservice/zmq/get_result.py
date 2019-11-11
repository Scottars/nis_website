


import os
dirPath = "." #所有txt位于的文件夹路径
files = os.listdir(dirPath)
res = ""
i = 0
for file in files:
    if file.endswith(".txt"):
        i += 1
        title = "第%s章 %s" % (i, file[0:len(file)-4])

        with open(file, "r", encoding='utf-8') as file:
            content = file.read()
            file.close()

        append = "\n%s\n\n%s" % (title,content)
        # append = "\n%s\n\n%s" % (title, content)
        res += append

with open("./testresult/testresult.txt", "w", encoding='utf-8') as outFile:
    outFile.write(res)
    outFile.close()
print(len(res))










