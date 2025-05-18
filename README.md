# Inkryptor

Inkryptor is a simple encryption tool for both images and text. It provides a user-friendly interface for encrypting images using a XOR-based algorithm and text using the Caesar cipher.

<div align="center">
    <img src="https://github.com/user-attachments/assets/c6afac89-bfaf-4583-9e6d-78052229aa54" alt="Logo" width="300" height="300">
</div>

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

## Screenshots

![Image XOR Encryption](https://private-user-images.githubusercontent.com/29468096/444905845-aabc0a0a-b5a0-4ddb-b5af-ace5a06fd65c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1ODY4MjMsIm5iZiI6MTc0NzU4NjUyMywicGF0aCI6Ii8yOTQ2ODA5Ni80NDQ5MDU4NDUtYWFiYzBhMGEtYjVhMC00ZGRiLWI1YWYtYWNlNWEwNmZkNjVjLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTE4VDE2NDIwM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWJhMmM4ZTQ1M2VkN2ZjNzE1NTUwOWQyZjA1YTk5Y2ZmODE1YWNjM2I1Yjk1MzUxMWY3ZDM0OTE2MGM4MDU2ODgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.j1dGRCX91Do63kbcmjtkmwtJEGYKqRJ_-2AFHUDY99U)

![Text Encryption](https://private-user-images.githubusercontent.com/29468096/444905865-fb3ea22d-fc22-465e-ae69-2689c129a027.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDc1ODY3OTIsIm5iZiI6MTc0NzU4NjQ5MiwicGF0aCI6Ii8yOTQ2ODA5Ni80NDQ5MDU4NjUtZmIzZWEyMmQtZmMyMi00NjVlLWFlNjktMjY4OWMxMjlhMDI3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA1MTglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNTE4VDE2NDEzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRhNzFkMzBhODdlODZhZGMzNGQ1OGQ4NjlhYzU5MWVlNjU1YzMzZDk3OThjM2I2ZTZkMmI3NjJmZDJjMWQzNTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.tDxWciyfcWuFVptvZfpKIZi6ZV_wu6oUb5IY--dyeEE)

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
