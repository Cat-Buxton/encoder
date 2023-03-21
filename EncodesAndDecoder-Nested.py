import random

while True:

    alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E":4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, \
                "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "-": 26}

    pick = input("!Q to quit.\n!E to encode in Ceasar.\n!D to decode in Ceasar.\n!SE to encode in seeded Ceasar.\n!SD to decode in seeded Ceasar.\n" ).upper()
    if pick[0] == '!':
        if 'Q' in pick[1]:
            exit()
        elif 'E' in pick[1]:
            message = input("For spaces, please use -\nPlease type a message to encode: ").upper()
            if all(char in alphabet for char in message):
                chars = list(message)
                print("original characters:", chars)
                nums1 = [alphabet[char] for char in chars]
                print("corresponding dictionary values:", nums1)
                offset = input("How many characters would you like to offset your message by? ")
                if offset.isdigit():
                    nums2 = []
                    for num in nums1:
                        nums2.append((num + int(offset)) % 27)
                    print("corresponding dictionary values + offset:", nums2)
                    alphabet_rev = {value: key for key, value in alphabet.items()}
                    message_e = [alphabet_rev[num] for num in nums2]
                    print("(corresponding dictionary values + offset) to letters:", message_e)
                    result = ''.join(message_e)
                    print("ENCODED MESSAGE: " + result)
                else:
                    print("Please input an integer, thank you.")
                    continue
            else:
                print("Please do not include numbers, special characters, or spaces. Thank you.")
                continue
        elif 'S' in pick[1]:
            if 'E' in pick[2]:
                message = input("For spaces, please use -\nPlease type a message to encode: ").upper()
                if all(char in alphabet for char in message):
                    chars = list(message)
                    print("original characters:", chars)
                    nums1 = [alphabet[char] for char in chars]
                    print("corresponding dictionary values:", nums1)
                    seed = [random.randint(1, 100) for _ in range(len(nums1))]
                    print("SEED:", '-'.join(map(str, seed)))
                    nums2 = []
                    nums2 = [(num + s) % 27 for num, s in zip(nums1, seed)]
                    print("corresponding dictionary values + seed:", nums2)
                    alphabet_rev = {value: key for key, value in alphabet.items()}
                    message_e = [alphabet_rev[num] for num in nums2]
                    print("(corresponding dictionary values + seed) to letters:", message_e)
                    result = ''.join(message_e)
                    print("ENCODED MESSAGE: " + result)
                else:
                    print("Please do not include numbers, special characters, or spaces. Thank you.")
                    continue
            elif 'D' in pick[2]:
                message = input("For spaces, please use -\nPlease type a message to decode: ").upper()
                if all(char in alphabet for char in message):
                    chars = list(message)
                    print("original characters:", chars)
                    nums1 = [alphabet[char] for char in chars]
                    print("corresponding dictionary values:", nums1)
                    seed = input("What was the seed of the original message? ")
                    if all(char.isdigit() or char == '-' for char in seed):
                        seed = [int(num) for num in seed.split("-")]
                        if len(seed) == len(nums1):    
                            nums2 = [(num - s) % 27 for num, s in zip(nums1, seed)]
                            print("corresponding dictionary values - seed:", nums2)
                            alphabet_rev = {value: key for key, value in alphabet.items()}
                            message_e = [alphabet_rev[num] for num in nums2]
                            print("(corresponding dictionary values - seed) to letters:", message_e)
                            result = ''.join(message_e)
                            print("DECODED MESSAGE: " + result)
                    else:
                        print("Please input a seed the length of the message, thank you.")
                        continue
                elif '' in pick[2]:
                    print("Not a command.")
                    continue
                else:
                    print("Please input a set of integers seperated by -, thank you.")
                    continue
            else:
                print("Not a command.")
                continue
        elif 'D' in pick[1]:
            message = input("For spaces, please use -\nPlease type a message to decode: ").upper()
            if all(char in alphabet for char in message):
                chars = list(message)
                print("original characters:", chars)
                nums1 = [alphabet[char] for char in chars]
                print("corresponding dictionary values:", nums1)
                offset = input("How many characters was the original message offset by? ")
                if offset.isdigit():
                    nums2 = []
                    for num in nums1:
                        nums2.append((num - int(offset)) % 27)
                    print("corresponding dictionary values + offset:", nums2)
                    alphabet_rev = {value: key for key, value in alphabet.items()}
                    message_e = [alphabet_rev[num] for num in nums2]
                    print("(corresponding dictionary values + offset) to letters:", message_e)
                    result = ''.join(message_e)
                    print("DECODED MESSAGE: " + result)
                else:
                    print("Please input an integer, thank you.")
                    continue
            else:
                print("Please do not include numbers, special characters, or spaces. Thank you.")
                continue
        else:
            print("Not a command.")
            continue
    else:
        print("Not a command.")
        continue
