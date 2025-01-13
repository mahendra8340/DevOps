import os as s


folder_list=input("Enter list of folder names: ").split()

for folder in folder_list:
    try:
        files=s.listdir(folder)
    except FileNotFoundError:
        print(f"Folder {folder} not found")
        continue
    except PermissionError:
        print(f"Permission denied for the folder {folder}")
        continue
    except Exception as e:
        print(f"Error: {e}")
        continue
    print(f"=============Files in {folder} are: =================")
    for file in files:
        print(file)