import sys


def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            print(f"{command}: command not found")

        except EOFError:
            print()
            break


if __name__ == "__main__":
    main()
