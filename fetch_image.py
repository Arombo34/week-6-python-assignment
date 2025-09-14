
import requests
import os
import webbrowser

# 1. Create a folder to store images
SAVE_FOLDER = "downloaded_images"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# 2. List of image URLs
IMAGE_URLS = [
    "https://www.python.org/static/img/python-logo.png",   # Python official logo
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",  # Mountain image
    "https://picsum.photos/400/300"  # Random placeholder image
]

# 3. Function to download and save images
def download_image(url, folder=SAVE_FOLDER):
    try:
        response = requests.get(url, timeout=10)  # Fetch image from URL
        response.raise_for_status()  # Raise error if request fails
        
        # Extract filename (fallback: use default name if URL doesn’t end with a file)
        filename = url.split("/")[-1]
        if not filename or "." not in filename:
            filename = "image_" + str(abs(hash(url))) + ".jpg"
        
        filepath = os.path.join(folder, filename)
        
        # Save the image to file
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        print(f"✅ Image saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Failed to download {url}: {e}")
        return None

# 4. Download all images
saved_files = []
for url in IMAGE_URLS:
    file = download_image(url)
    if file:
        saved_files.append(file)

# 5. Automatically open downloaded images in the default viewer (optional)
for img in saved_files:
    webbrowser.open("file://" + os.path.abspath(img))

print("\n📌 Task complete! Images are in the 'downloaded_images' folder.")
