
# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher.\n")
print("When creating your message, you may only choose from the following characters: " + possibleCharacters + "\n")
print("Let's get started!\n")

print()
while True:  # Start an infinite loop
    shiftedMessage = ""  # Reset shiftedMessage for each new message

    # Receive user input
    initialMessage = input("What is your message? ")
    print()
    key = int(input("What is the key? Choose a number from 0 to 25. "))
    print()
    mode = input("Do you want to encrypt or decrypt? ")

    # Add a blank line for spacing
    print()

    # Encrypt or decrypt the message
    for character in initialMessage:
       if character in possibleCharacters:  # Check if the character is in the allowed set
            # Determine the case and position of the character
            initialPosition = possibleCharacters.find(character)
            if character.isupper() or character == ' ':
                # Wrap within uppercase or space
                shiftedPosition = (initialPosition + key) % 27  # Adjusted for space
            else:
                # Wrap within lowercase
                shiftedPosition = (initialPosition + key) % 27 + 27  # Adjusted for space and lowercase

            if mode.lower() == "decrypt":
                # Adjust for decrypt mode
                if character.isupper() or character == ' ':
                    shiftedPosition = (initialPosition - key) % 27  # Adjusted for space
                else:
                    shiftedPosition = (initialPosition - key) % 27 + 27  # Adjusted for space and lowercase

            shiftedMessage += possibleCharacters[shiftedPosition]
       else:
            shiftedMessage += character  # Append non-allowed characters without changes
    print()
    # Print the shifted message with an extra blank line before and after for spacing
    print("\nYour " + mode.lower() + "ed message is: " + shiftedMessage + "\n")
    
    # Ask the user if they want to continue or exit, with a blank line after for spacing
    continue_program = input("Do you want to encrypt or decrypt another message? (yes/no) ").lower()
    print()
    if continue_program != 'yes':
        break  # Exit the loop if the user does not want to continue

print("Thank you for using the Caesar cipher program. Goodbye!")