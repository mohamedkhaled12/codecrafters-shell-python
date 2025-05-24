import sys


def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
        except EOFError:
            print()
            break
        if command.strip() == "exit 0":
            sys.exit(0)
        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
