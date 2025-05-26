import sys
import os
import subprocess

# Function to handle the `type` command
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

# Built-in commands dictionary
BUILTINS = {
    "exit": lambda code=0, *_: sys.exit(int(code)),
    "echo": lambda *args: print(" ".join(args)),
    "type": type_cmd,
}

# Main shell loop
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        try:
            user_input = input().split()
            if not user_input:
                continue

            cmd = user_input[0]
            args = user_input[1:]

            if cmd in BUILTINS:
                BUILTINS[cmd](*args)
            else:
                found = False
                for directory in os.getenv("PATH", "").split(":"):
                    full_path = os.path.join(directory, cmd)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        # ✅ Fixed part: ensure argv[0] is just the command name
                        subprocess.run([cmd] + args, executable=full_path)
                        found = True
                        break
                if not found:
                    print(f"{cmd}: command not found")

        except EOFError:
            break
        except KeyboardInterrupt:
            print()  # Print newline on Ctrl+C
            continue

if __name__ == "__main__":
    main()
