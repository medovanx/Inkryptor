# Inkryptor

Inkryptor is a simple encryption tool for both images and text. It provides a user-friendly interface for encrypting images using a XOR-based algorithm and text using the Caesar cipher.

## Features

### Image Encryption
- Load and display images
- Encrypt and decrypt images using a XOR-based algorithm
- View histograms of the original and processed images
- Save the encrypted/decrypted images

### Text Encryption
- Encrypt and decrypt text using the Caesar cipher
- Specify the shift key for encryption/decryption
- Clear text function for convenience

## Setup Instructions

1. Install Python 3.x if not already installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python main.py
   ```

## How to Use

### Image Encryption
1. Click on "Load Image" to select an image from your file system
2. Enter an encryption key (any string or number)
3. Click "Encrypt" to encrypt the image
4. Click "Decrypt" to decrypt the image using the same key
5. Click "Save Image" to save the processed image to your file system

### Text Encryption
1. Enter the text to encrypt/decrypt in the "Original Text" field
2. Set the Caesar shift key (1-25)
3. Click "Encrypt" or "Decrypt" to process the text
4. The result will appear in the "Processed Text" field
5. Click "Clear" to clear both text fields

## Note
This application is developed for educational purposes only. The encryption methods used are not secure for sensitive data.
