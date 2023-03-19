# While true is true (true will always be true).
while True:

    # Create a dictionary assigning a number to each uppercase letter, with - (psuedo space character) as its own character with its own value.
    alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E":4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, \
                "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, "-": 26}

    # As the user to input a message then convert the message to uppercase letters.
    message = input("Type !Q to quit.\nFor spaces, please use -\nPlease type a message to decode: ").upper()
    
    # If the inputted message contains characters that are within the dictionary, follow through.
    if all(char in alphabet for char in message):
        # Create a list using each character from the inputted message. 
        chars = list(message)
        # Display the inputted message.
        print("original characters:", chars)

        # Convert each character in the list of characters to their corresponding dictionary value.
        nums1 = [alphabet[char] for char in chars]
        # Display the corresponding dictionary values.
        print("corresponding dictionary values:", nums1)

        # Ask the user for the offset.
        offset = input("How many characters was the original message offset by? ")
        # If the inputted offset is a digit (ex. 1, 13, 5...), follow through.
        if offset.isdigit():
            # Create an empty list.
            nums2 = []
            # For each number in the list of numbers (nums1) subtract the inputted offset. 
            # However, if the number plus the offset goes above the number of keys/values in the dictionary (26), go back to the value of 0 before continuing.
            for num in nums1:
                nums2.append((num - int(offset)) % 27)
            # Display the corresponding dictionary values plus the offset.
            print("corresponding dictionary values + offset:", nums2)
            
            # Take the original alphabet dictionary and map the values (0 to 26) to the characters (A to -) through reversing.
            alphabet_rev = {value: key for key, value in alphabet.items()}
            
            # Take the list of corresponding dictionary values + offset and convert them to characters using the reverse dictionary.
            message_e = [alphabet_rev[num] for num in nums2]
            # Display the corresponding dictionary values plus the offset to characters.
            print("(corresponding dictionary values + offset) to letters:", message_e)
            # To convert the list to a string by joining the list together.
            result = ''.join(message_e)
            # Print the final result.
            print("Decoded message: " + result)
        # If the inputted offset is not a digit, restart.
        else:
            print("Please input an integer, thank you.")
            continue
    # If the user types !q, quit.
    elif message[0] == '!':
        if 'Q' in message[1]:
            exit()
    # If the original inputted message (message) contains characters that are outside of the dictionary, restart.
    else:
        print("Please do not include numbers, special characters, or spaces. Thank you.")
        continue
