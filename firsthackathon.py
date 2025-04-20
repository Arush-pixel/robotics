import sys
import time

def main():
    name = input("What is your name? ")
    print("Hello,")
    for char in name:
        if 'r' in char.lower():
            print("red")
        if 'b' in char.lower():
                    print("blue")
        if 'g' in char.lower():
            print("green")
    

    print("!")

if __name__ == "__main__":
    main()
