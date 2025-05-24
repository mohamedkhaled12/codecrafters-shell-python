import sys

def main():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()

            if command.strip() == "exit 0":
                sys.exit(0)
            
            if command == "type":
                print(f"{command}: command not found")

            if ' ' in command:
                first_part, rest_to_be_handled = command.split(' ', 1)
                if first_part == 'echo':
                    print(rest_to_be_handled)
                    continue  # Skip printing "command not found"
                if first_part == 'type':
                    print(f"{rest_to_be_handled} is a shell builtin")
                

            print(f"{command}: command not found")

        except EOFError:
            print()
            break

if __name__ == "__main__":
    main()
