"""
In other words, write it inside triple quotes like this
and place it right in the beginning of your program file.
Initial comment should explain who wrote the program and
what does it do.
"""

def main():
    num = int(input("How many Fibonacci numbers do you want? "))

    fib1 = 0
    fib2 = 1
    print(f"1. {fib2}")
    i = 2
    while i <= num:
        new_fib = fib1 + fib2

        fib1 = fib2
        fib2 = new_fib
        print(f"{i}. {new_fib}")

        i += 1


if __name__ == "__main__":
    main()