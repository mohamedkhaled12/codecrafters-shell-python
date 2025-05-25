import sys
import os

def type_cmd(cmd, *_):
    if cmd in BUILTINS:
        print(f"{cmd} is a shell builtin")
    else:
        for directory in os.getenv("PATH", "").split(":"):
            full_path = os.path.join(directory, cmd)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                print(f"{cmd} is {full_path}")
                return
        print(f"{cmd}: not found")
                
            
        
    

BUILTINS = {
    "exit": lambda code=0, *_: sys.exit(int(code)),
    "echo": lambda *args : print(" ".join(args)),
    "type": type_cmd,
}


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        user_input = input().split()
        cmd = user_input[0]
        args = user_input[1:]
        
        if cmd in BUILTINS:
            BUILTINS[cmd](*args)
        else:
            print(f"{cmd}: command not found")    
        


if __name__ == "__main__":
    main()
        