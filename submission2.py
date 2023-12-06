"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""

def main():
    name = str(input("Tell us your name: "))
    print("Hey ", end=name)
    print(", the printout formatting is going well!")


if __name__ == "__main__":
    main()