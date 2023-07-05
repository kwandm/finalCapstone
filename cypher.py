def encode_message(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            ascii_value = ord(char.lower())  # Convert the letter to its ASCII value
            encoded_ascii = (ascii_value - 97 + 15) % 26 + 97  # Apply the cipher rule
            encoded_char = chr(encoded_ascii)  # Convert the ASCII value back to a character
            if char.isupper():  # Preserve the original casing
                encoded_char = encoded_char.upper()
        else:
            encoded_char = char  # Preserve non-alphabetic characters
        encoded_message += encoded_char
    return encoded_message

# Prompt the user for a message to encode
message = input("Enter a message to encode: ")

# Encode the message
encoded_message = encode_message(message)

# Print the encoded message
print("Encoded message:", encoded_message)
