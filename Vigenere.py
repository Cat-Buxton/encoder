while True:

    alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E":4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, \
                "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "-": 26}
    
    pick = input("!Q to quit.\n!VE to encode in modified Vigenere.\n!VD to decode in modified Vigenere.\n" ).upper()
    if pick[0] == "!":
        if "Q" in pick[1]:
            exit()
        elif "V" in pick[1]:
            if "E" in pick[2]:
                message = input("For spaces, please use -\nPlease type a message to encode: ").upper()
                k = input("For spaces, please use -\nPlease type a key: ").upper()
                if all(char in alphabet for char in message) and all(char in alphabet for char in k):
                    chars = list(message)
                    print("original characters: ", chars)
                    key_chars = list(k)
                    nums1 = [alphabet[char] for char in chars]
                    print("corresponding dictionary values:", nums1)
                    nums2 = [alphabet[char] for char in key_chars]
                    wrapped_key = [nums2[i % len(nums2)] for i in range(len(nums1))]
                    print("wrapped key to corresponding dictionary values: ", wrapped_key)
                    nums3 = [(num + s) % 27 for num, s in zip(nums1, wrapped_key)]
                    print("corresponding dictionary values + key to corresponding dictionary values: ", nums3)
                    alphabet_rev = {value: key for key, value in alphabet.items()}
                    message_e = [alphabet_rev[num] for num in nums3]
                    print("(corresponding dictionary values + key to corresponding dictionary values) to letters:", message_e)
                    result = ''.join(message_e)
                    print("ENCODED MESSAGE: " + result)
                else:
                    print("Please do not include numbers, special characters, or spaces. Thank you.")
                    continue
            elif "D" in pick[2]:
                message = input("For spaces, please use -\nPlease type a message to decode: ").upper()
                k = input("For spaces, please use -\nWhat was the key of the original message?: ").upper()
                if all(char in alphabet for char in message) and all(char in alphabet for char in k):
                    chars = list(message)
                    print("original characters: ", chars)
                    key_chars = list(k)
                    nums1 = [alphabet[char] for char in chars]
                    print("corresponding dictionary values:", nums1)
                    nums2 = [alphabet[char] for char in key_chars]
                    wrapped_key = [nums2[i % len(nums2)] for i in range(len(nums1))]
                    print("wrapped key to corresponding dictionary values: ", wrapped_key)
                    nums3 = [(num - s) % 27 for num, s in zip(nums1, wrapped_key)]
                    print("corresponding dictionary values + key to corresponding dictionary values: ", nums3)
                    alphabet_rev = {value: key for key, value in alphabet.items()}
                    message_e = [alphabet_rev[num] for num in nums3]
                    print("(corresponding dictionary values + key to corresponding dictionary values) to letters:", message_e)
                    result = ''.join(message_e)
                    print("DECODED MESSAGE: " + result)
                else:
                    print("Please do not include numbers, special characters, or spaces. Thank you.")
                    continue
            else:
                print("Not a valid command.")
                continue
        else:
            print("Not a valid command.")
            continue
    else:
        print("Not a valid command.")
        continue