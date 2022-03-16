import shutil
import os
# os.system("date")
# os.mkdir("/Users/DELL/Desktop/Coding/newfolder")
path = input("Enter The Name OF The Directory To Be Sorted: ")
listOfFiles = os.listdir(path)
print(listOfFiles)
for filename in listOfFiles:
    name, ext = os.path.splitext(filename)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + filename, path + "/" + ext + "/" + filename)
    else:
        os.mkdir(path + "/" + ext)
        shutil.move(path + "/" + filename, path + "/" + ext + "/" + filename)
        
