import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
