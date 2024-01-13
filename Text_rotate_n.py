# OP3N1T SECURITY
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--text", help="Text", type=str)
parser.add_argument("-r", "--rotation", help="Rotation", type=str)
args = parser.parse_args()

PURPLE = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


print(" ")
print(f"{YELLOW}WELCOME TO TEXT ROTATOR !{RESET}")
print("---------------------------------")

def rot_n(text, n):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:
            new_char = char
        result += new_char
    return result

text_to_encrypt = input(f"{RED}Enter the sentence to encode: {RESET}")
rotation = int(input(f"{PURPLE}Enter the rotation number: {RESET}"))

encrypted_text = rot_n(text_to_encrypt, rotation)
print(f"{GREEN}Encrypted Text: {RESET}", encrypted_text)
print("---------------------------------")
