import os
from PIL import Image

# Path to your downloaded image
image_path = os.path.join("Assets", "black_spaceship.png")

if not os.path.exists(image_path):
    print(f"Error: Could not find the file at {image_path}")
    print("Please make sure you are running this script from your project root folder.")
else:
    try:
        # Open and inspect the image structure
        with Image.open(image_path) as img:
            print("File Found!")
            print(f"  - Claimed Extension: .png")
            print(f"  - Actual Internal Format: {img.format}")
            print(f"  - Dimensions: {img.size}")
            
            # Re-save it strictly as a real PNG
            img.save(image_path, "PNG")
            print("Success! The file has been successfully re-encoded as a proper PNG.")

    except IOError:
        # If Pillow can't read it, it is likely an HTML page or completely corrupted
        print("Error: The file data is completely unreadable as an image.")
        print("This usually happens if you downloaded an HTML webpage by accident.")
        
        # Read the first few characters to check if it's text/HTML
        with open(image_path, "r", encoding="utf-8", errors="ignore") as f:
            sample = f.read(100)
            if "<html" in sample.lower() or "<!doctype" in sample.lower():
                print("\nConfirmed: This file contains HTML web code, not image data!")
import os
from PIL import Image

# Path to your downloaded image
image_path = os.path.join("Assets", "black_spaceship.png")

if not os.path.exists(image_path):
    print(f"Error: Could not find the file at {image_path}")
    print("Please make sure you are running this script from your project root folder.")
else:
    try:
        # Open and inspect the image structure
        with Image.open(image_path) as img:
            print("File Found!")
            print(f"  - Claimed Extension: .png")
            print(f"  - Actual Internal Format: {img.format}")
            print(f"  - Dimensions: {img.size}")
            
            # Re-save it strictly as a real PNG
            img.save(image_path, "PNG")
            print("Success! The file has been successfully re-encoded as a proper PNG.")

    except IOError:
        # If Pillow can't read it, it is likely an HTML page or completely corrupted
        print("Error: The file data is completely unreadable as an image.")
        print("This usually happens if you downloaded an HTML webpage by accident.")
        
        # Read the first few characters to check if it's text/HTML
        with open(image_path, "r", encoding="utf-8", errors="ignore") as f:
            sample = f.read(100)
            if "<html" in sample.lower() or "<!doctype" in sample.lower():
                print("\nConfirmed: This file contains HTML web code, not image data!")
