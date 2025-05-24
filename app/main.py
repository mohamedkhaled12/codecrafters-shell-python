import sys


def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while True:
        try:
            sys.stdout.write("$ ")
            command = input()
            echo_part, rest_to_be_echoed = command.split(' ', 1)

            if echo_part == 'echo':
                print(f"{rest_to_be_echoed}")
        except EOFError:
            print()
            break
        if command.strip() == "exit 0":
            sys.exit(0)
        


if __name__ == "__main__":
    main()
