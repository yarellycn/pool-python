import os

# os.chdir("path")

# (os.listdir())       #List files and directory


# os.path.isfile(path): returns True if the path is a valid file
# os.path.isdir(path): returns True if the path is a valid directory
# os.path.exists(path) : returns True if the path is a valid file or directory

def readdir(path, current_folder):
    print(f"{current_folder}:")
    directory = os.listdir(path)
    directory = list(filter(lambda x: not x[0] == ".", directory))
    for item in directory:
        print(item, end= " ")
    print("")
    for item in directory:
        if os.path.isdir(path + "/" + item):
            print("")
            readdir(path + "/" + item, current_folder + "/" + item)
        


cwd = os.getcwd()       #Gets current path
readdir(cwd, ".")