import cv2
from PyQt5.QtGui import QImage, QPixmap
import io
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


class ImageProcessor:
    def __init__(self):
        self.original_image = None
        self.processed_image = None
        self.current_key = 0

    def load_image(self, file_path):
        """Load an image from the given file path"""
        try:
            self.original_image = cv2.imread(file_path)
            if self.original_image is None:
                return False, "Failed to load image"
            return True, self.original_image
        except Exception as e:
            return False, str(e)

    def xor_encrypt_decrypt(self, image, key):
        """Simple XOR encryption/decryption of an image"""
        # Convert key to integer if it's a string
        if isinstance(key, str):
            try:
                numeric_key = sum(ord(c) for c in key)
            except:
                numeric_key = 123  # Default key
        else:
            numeric_key = key

        # Create a copy of the image to avoid modifying the original
        result = image.copy()

        # Apply XOR operation to each pixel value
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                # XOR each channel with the key
                for k in range(result.shape[2]):
                    result[i, j, k] = result[i, j, k] ^ (numeric_key)

        return result

    def encrypt_image(self, key):
        """Encrypt the original image using XOR with the given key"""
        if self.original_image is None:
            return False, "No image loaded"

        try:
            self.processed_image = self.xor_encrypt_decrypt(
                self.original_image, key)
            self.current_key = key
            return True, self.processed_image
        except Exception as e:
            return False, str(e)

    def decrypt_image(self, key):
        """Decrypt the processed image using XOR with the given key"""
        if self.processed_image is None:
            return False, "No processed image available"

        try:
            # For XOR, encryption and decryption are the same operation
            decrypted = self.xor_encrypt_decrypt(self.processed_image, key)
            self.processed_image = decrypted
            return True, decrypted
        except Exception as e:
            return False, str(e)

    def save_image(self, file_path):
        """Save the processed image to the given file path"""
        if self.processed_image is None:
            return False, "No processed image to save"

        try:
            result = cv2.imwrite(file_path, self.processed_image)
            if not result:
                return False, "Failed to save image"
            return True, "Image saved successfully"
        except Exception as e:
            return False, str(e)

    def get_histogram_pixmap(self, image):
        """Generate histogram of the image and return as QPixmap"""
        if image is None:
            return None

        try:
            # Create a figure for the histogram
            fig = Figure(figsize=(5, 4), dpi=100)
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)

            # Calculate histograms for each channel
            colors = ('b', 'g', 'r')
            for i, color in enumerate(colors):
                hist = cv2.calcHist([image], [i], None, [256], [0, 256])
                ax.plot(hist, color=color)

            ax.set_xlim([0, 256])
            ax.grid(True)
            fig.tight_layout()

            # Convert to QPixmap
            canvas.draw()
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)

            img = QImage.fromData(buf.getvalue())
            pixmap = QPixmap.fromImage(img)

            return pixmap

        except Exception as e:
            print(f"Error generating histogram: {str(e)}")
            return None

    def cv_to_qpixmap(self, cv_img):
        """Convert OpenCV image to QPixmap"""
        if cv_img is None:
            return None

        try:
            # Convert the image from BGR (OpenCV) to RGB (Qt)
            rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w

            # Create QImage from the RGB data
            q_img = QImage(rgb_image.data, w, h,
                           bytes_per_line, QImage.Format_RGB888)

            # Convert QImage to QPixmap
            return QPixmap.fromImage(q_img)
        except Exception as e:
            print(f"Error converting image: {str(e)}")
            return None
