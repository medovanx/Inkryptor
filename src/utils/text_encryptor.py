class TextEncryptor:
    def __init__(self):
        pass
    
    def caesar_encrypt(self, text, shift):
        """
        Encrypt the given text using Caesar cipher with the specified shift
        
        Args:
            text (str): The text to encrypt
            shift (int): The shift key (1-25)
            
        Returns:
            str: The encrypted text
        """
        result = ""
        
        # Loop through each character in the input text
        for char in text:
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + shift - 97) % 26 + 97)
            # non-alphabetic characters
            else:
                result += char
                
        return result
    
    def caesar_decrypt(self, text, shift):
        """
        Decrypt the given text using Caesar cipher with the specified shift
        
        Args:
            text (str): The text to decrypt
            shift (int): The shift key (1-25)
            
        Returns:
            str: The decrypted text
        """
        # For decryption, we use the same algorithm with a negative shift
        return self.caesar_encrypt(text, (26 - shift) % 26)
