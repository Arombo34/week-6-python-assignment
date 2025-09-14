# week-6-python-assignment
🌍 Ubuntu Image Fetcher

"I am because we are" – Ubuntu Philosophy

This project is a simple but meaningful Python script that fetches images from the web, organizes them, and saves them for later use — all while embracing the principles of community, respect, sharing, and practicality.

✨ Features

Fetches images from the internet using the requests library

Saves images in a folder called Fetched_Images

Extracts filenames automatically or generates them if missing

Handles network errors gracefully (timeouts, invalid links, HTTP errors)

Skips duplicate images using content hashing

Checks HTTP headers to ensure only images are saved

Preloaded with sample image URLs for quick testing

📦 Requirements

Python 3.x

requests library

Install dependencies:

pip install requests

🚀 Usage

Run the script:

python fetch_image.py


It will automatically fetch these sample images:

Python Logo

NASA Astronomy Picture

Placeholder Image

✅ Images will be saved inside the Fetched_Images folder.

🧩 Example Output
🌍 Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

✓ Successfully fetched: python-logo-master-v3-TM.png
✓ Image saved to Fetched_Images/python-logo-master-v3-TM.png

✓ Successfully fetched: IC405_Abolfath_3952.jpg
✓ Image saved to Fetched_Images/IC405_Abolfath_3952.jpg

✓ Successfully fetched: 300
✓ Image saved to Fetched_Images/300

👋 Done! Connection strengthened. Community enriched.

🕊 Ubuntu Principles in Action

Community → Connects to the wider internet to fetch shared resources.

Respect → Handles errors gracefully without crashing.

Sharing → Organizes images for later use and sharing.

Practicality → A simple, useful tool for mindful browsing.

"A person is a person through other persons." – Ubuntu

📂 Repository Structure
Ubuntu_Requests/
│
├── fetch_image.py   # Main script
├── README.md        # Documentation
└── Fetched_Images/  # Saved images (created automatically)

👨‍💻 Author

Created by Wycliffe Arombo in the spirit of Ubuntu 🖤
