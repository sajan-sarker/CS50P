"""format name using regex"""
import re

def swap_name(name):
    pattern = r"^(.+), *(.+)$"
    matches = re.search(pattern, name)
    if matches:
        name = matches.group(2) + " " + matches.group(1)
    return name

def main():
    name = str(input("Enter your name: ")).strip().title()
    full_name = swap_name(name)
    print("Hola,", full_name)

if __name__ == "__main__":
    main()