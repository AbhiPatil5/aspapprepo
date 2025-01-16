import os

number=input("Enter Number:")
print("You entered- ",number)

foldernames=input("Enter foldersnames to check with space:").split(" ")
print("/",foldernames)

for fname in foldernames:
    folder = os.path.join(os.getcwd(), fname)
    print("Processing folder -", folder)
    try:
        files = os.listdir(folder)
        print("Files in folder -", files)
    except FileNotFoundError:
        print(f"Folder {folder} not found.")
    except PermissionError:
        print(f"Permission denied for folder {folder}.")
    