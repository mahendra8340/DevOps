import sys

def update_server_config(file_path, property, value):
    try:
        with open(file_path,"r") as file:
            lines =file.readlines() 
    except FileNotFoundError:
        print(f"{file_path} not found")
        return False
    
    with open(file_path,"w") as file:
        for line in lines:
            if(property in line):
                file.write(f"{property}={value}\n")
            else:
                file.write(line)
    return True


if(len(sys.argv)!=4):
    print("Usage: python update_config.py <file_path> <property> <value>")
    sys.exit(1)

result= update_server_config(sys.argv[1],sys.argv[2],sys.argv[3])
#result= update_server_config("server.conf", "PORT", "8089")
if result:
    print("Config updated successfully")