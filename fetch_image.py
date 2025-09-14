import requests
import os
import hashlib
from urllib.parse import urlparse

# Folder for saving images
FOLDER = "Fetched_Images"

# Preloaded image URLs (you can add more here)
IMAGE_URLS = [
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    "https://apod.nasa.gov/apod/image/1901/IC405_Abolfath_3952.jpg",
    "https://picsum.photos/400/300"
]

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_already_exists(content, folder=FOLDER):
    """Check if a file with the same content already exists to prevent duplicates."""
    new_hash = hashlib.md5(content).hexdigest()
    for existing_file in os.listdir(folder):
        existing_path = os.path.join(folder, existing_file)
        with open(existing_path, "rb") as f:
            if hashlib.md5(f.read()).hexdigest() == new_hash:
                return True
    return False

def fetch_image(url):
    """Fetch and save an image from a URL."""
    try:
        # Fetch the image with headers for safety
        headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check content type header before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Ensure directory exists
        os.makedirs(FOLDER, exist_ok=True)

        # Prevent duplicate downloads
        if file_already_exists(response.content):
            print(f"✗ Duplicate skipped: {url}")
            return

        # Determine filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(FOLDER, filename)

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("🌍 Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Loop through preloaded URLs
    for url in IMAGE_URLS:
        fetch_image(url)

    print("👋 Done! Connection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
