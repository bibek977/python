fileName=input("Enter a file name: ")
file_ext=fileName.split(".")
print(file_ext)
print(file_ext[-1])

if file_ext[-1]=="py":
    print("The file is PYTHON file.")
if file_ext[-1]=="txt":
    print("The file is TEXT File")
if file_ext[-1]=="html":
    print("The file is HTML File")
if file_ext[-1]=="css":
    print("The file is CSS File")
if file_ext[-1]=="txt":
    print("The file is JAVASCRIPT File")

