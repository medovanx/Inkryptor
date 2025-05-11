import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.ui.app_controller import InkryptorApp

if __name__ == "__main__":
    app = InkryptorApp()
    sys.exit(app.run())
