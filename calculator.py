while True:
    user_input = input("> ")
    
    if "+" in user_input:
        sep = user_input.split("+")
        print(int(sep[0]) + int(sep[1]))
    
    if "-" in user_input:
        sep = user_input.split("-")
        print(int(sep[0]) - int(sep[1]))
        
    if "*" in user_input:
        sep = user_input.split("*")
        print(int(sep[0]) * int(sep[1]))
        
    if "/" in user_input:
        sep = user_input.split("/")
        print(int(sep[0]) / int(sep[1]))
        