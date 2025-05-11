import sys
import os
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.image_processor import ImageProcessor
from utils.text_encryptor import TextEncryptor


class InkryptorApp: 
    def __init__(self):
        # Load the UI file
        ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inkryptor.ui')
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = uic.loadUi(ui_file)
        
        # Initialize processors
        self.image_processor = ImageProcessor()
        self.text_encryptor = TextEncryptor()
        
        # Connect signals to slots
        self.setup_connections()

        # Instance variables
        self.image_path = None

    def setup_connections(self):
        """Connect UI signals to their respective slots"""
        # Image tab connections
        self.window.btnLoadImage.clicked.connect(self.load_image)
        self.window.btnEncryptImage.clicked.connect(self.encrypt_image)
        self.window.btnDecryptImage.clicked.connect(self.decrypt_image)
        self.window.btnSaveImage.clicked.connect(self.save_image)
        
        # Text tab connections
        self.window.btnEncryptText.clicked.connect(self.encrypt_text)
        self.window.btnDecryptText.clicked.connect(self.decrypt_text)
        self.window.btnClearText.clicked.connect(self.clear_text)
        
        # Menu connections
        self.window.actionExit.triggered.connect(self.window.close)
        self.window.actionAbout.triggered.connect(self.show_about)
        
    def load_image(self):
        """Load an image from the file system"""
        file_path, _ = QFileDialog.getOpenFileName(
            self.window,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        
        if file_path:
            self.image_path = file_path
            success, image = self.image_processor.load_image(file_path)
            
            if success:
                # Display the original image
                original_pixmap = self.image_processor.cv_to_qpixmap(image)
                if original_pixmap:
                    self.window.lblOriginalImage.setPixmap(
                        original_pixmap.scaled(
                            self.window.lblOriginalImage.width(),
                            self.window.lblOriginalImage.height(),
                            aspectRatioMode=1
                        )
                    )
                
                # Generate and display histogram for original image
                original_hist = self.image_processor.get_histogram_pixmap(image)
                if original_hist:
                    self.window.lblOriginalHistogram.setPixmap(
                        original_hist.scaled(
                            self.window.lblOriginalHistogram.width(),
                            self.window.lblOriginalHistogram.height(),
                            aspectRatioMode=1
                        )
                    )
                
                # Clear the processed image and histogram
                self.window.lblProcessedImage.setText("Processed Image")
                self.window.lblProcessedHistogram.setText("Processed Histogram")
                self.window.statusbar.showMessage(f"✅ Loaded image: {os.path.basename(file_path)}")
            else:
                QMessageBox.critical(self.window, "Error", f"Failed to load image: {image}")
    
    def encrypt_image(self):
        """Encrypt the loaded image"""
        if self.image_processor.original_image is None:
            QMessageBox.warning(self.window, "Warning", "Please load an image first")
            return
            
        key = self.window.txtImageKey.text()
        if not key:
            QMessageBox.warning(self.window, "Warning", "Please enter an encryption key")
            return
            
        success, processed = self.image_processor.encrypt_image(key)
        
        if success:
            # Display the encrypted image
            processed_pixmap = self.image_processor.cv_to_qpixmap(processed)
            if processed_pixmap:
                self.window.lblProcessedImage.setPixmap(
                    processed_pixmap.scaled(
                        self.window.lblProcessedImage.width(),
                        self.window.lblProcessedImage.height(),
                        aspectRatioMode=1
                    )
                )
            
            # Generate and display histogram for encrypted image
            processed_hist = self.image_processor.get_histogram_pixmap(processed)
            if processed_hist:
                self.window.lblProcessedHistogram.setPixmap(
                    processed_hist.scaled(
                        self.window.lblProcessedHistogram.width(),
                        self.window.lblProcessedHistogram.height(),
                        aspectRatioMode=1
                    )
                )
            
            self.window.statusbar.showMessage("🔒 Image encrypted successfully")
        else:
            QMessageBox.critical(self.window, "Error", f"Failed to encrypt image: {processed}")
    
    def decrypt_image(self):
        """Decrypt the processed image"""
        if self.image_processor.processed_image is None:
            QMessageBox.warning(self.window, "Warning", "Please encrypt an image first")
            return
            
        key = self.window.txtImageKey.text()
        if not key:
            QMessageBox.warning(self.window, "Warning", "Please enter the decryption key")
            return
            
        success, decrypted = self.image_processor.decrypt_image(key)
        
        if success:
            # Display the decrypted image
            decrypted_pixmap = self.image_processor.cv_to_qpixmap(decrypted)
            if decrypted_pixmap:
                self.window.lblProcessedImage.setPixmap(
                    decrypted_pixmap.scaled(
                        self.window.lblProcessedImage.width(),
                        self.window.lblProcessedImage.height(),
                        aspectRatioMode=1
                    )
                )
            
            # Generate and display histogram for decrypted image
            decrypted_hist = self.image_processor.get_histogram_pixmap(decrypted)
            if decrypted_hist:
                self.window.lblProcessedHistogram.setPixmap(
                    decrypted_hist.scaled(
                        self.window.lblProcessedHistogram.width(),
                        self.window.lblProcessedHistogram.height(),
                        aspectRatioMode=1
                    )
                )
            
            self.window.statusbar.showMessage("🔓 Image decrypted successfully")
        else:
            QMessageBox.critical(self.window, "Error", f"Failed to decrypt image: {decrypted}")
    
    def save_image(self):
        """Save the processed image to the file system"""
        if self.image_processor.processed_image is None:
            QMessageBox.warning(self.window, "Warning", "No processed image to save")
            return
            
        file_path, _ = QFileDialog.getSaveFileName(
            self.window,
            "Save Image",
            "",
            "PNG Image (*.png);;JPEG Image (*.jpg);;Bitmap Image (*.bmp)"
        )
        
        if file_path:
            success, message = self.image_processor.save_image(file_path)
            
            if success:
                self.window.statusbar.showMessage(f"💾 Image saved as: {os.path.basename(file_path)}")
            else:
                QMessageBox.critical(self.window, "Error", f"Failed to save image: {message}")
    
    def encrypt_text(self):
        """Encrypt the text using Caesar cipher"""
        text = self.window.txtOriginal.toPlainText()
        if not text:
            QMessageBox.warning(self.window, "Warning", "Please enter some text to encrypt")
            return
            
        shift = self.window.spinShiftKey.value()
        encrypted = self.text_encryptor.caesar_encrypt(text, shift)
        self.window.txtProcessed.setPlainText(encrypted)
        self.window.statusbar.showMessage(f"🔒 Text encrypted with shift {shift}")
    
    def decrypt_text(self):
        """Decrypt the text using Caesar cipher"""
        text = self.window.txtOriginal.toPlainText()
        if not text:
            QMessageBox.warning(self.window, "Warning", "Please enter some text to decrypt")
            return
            
        shift = self.window.spinShiftKey.value()
        decrypted = self.text_encryptor.caesar_decrypt(text, shift)
        self.window.txtProcessed.setPlainText(decrypted)
        self.window.statusbar.showMessage(f"🔓 Text decrypted with shift {shift}")
    
    def clear_text(self):
        """Clear the text fields"""
        self.window.txtOriginal.clear()
        self.window.txtProcessed.clear()
        self.window.statusbar.showMessage("🧹 Text cleared")
    
    def show_about(self):
        """Show the About dialog"""
        about_box = QMessageBox(self.window)
        about_box.setWindowTitle("About Inkryptor")
        about_box.setTextFormat(QtCore.Qt.RichText)
        about_box.setText("""<h1>Inkryptor v1.0</h1>
        <p>A simple encryption tool for images and text.</p>
        <p>This application demonstrates basic encryption techniques:</p>
        <ul>
            <li> XOR encryption for images</li>
            <li> Caesar cipher for text</li>
        </ul>
        <p>Created for educational purposes by <a href='https://github.com/medovanx'>Mohamed Darwesh</a></p>""")
        about_box.exec_()

    def run(self):
        self.window.show()
        self.window.statusbar.showMessage(
            "✨ Welcome to Inkryptor - Ready to secure your data ✨", 
        )
        return self.app.exec_()
