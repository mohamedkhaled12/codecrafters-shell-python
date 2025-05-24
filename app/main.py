import sys

def main():
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()

            if command.strip() == "exit 0":
                sys.exit(0)

            if ' ' in command:
                echo_part, rest_to_be_echoed = command.split(' ', 1)
                if echo_part == 'echo':
                    print(rest_to_be_echoed)
                    continue  # Skip printing "command not found"

            print(f"{command}: command not found")

        except EOFError:
            print()
            break

if __name__ == "__main__":
    main()
