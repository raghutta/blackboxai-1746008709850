import os
import requests
from PIL import Image
from io import BytesIO
import shutil

# Folder paths
mobile_folder = "wallpapers/wallpapers_for_mobile"
desktop_folder = "wallpapers/wallpapers_for_desktops"

# Create folders if not exist
os.makedirs(mobile_folder, exist_ok=True)
os.makedirs(desktop_folder, exist_ok=True)

# Wallpaper URLs for desktops (landscape)
desktop_wallpaper_urls = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1494526585095-c41746248156",
    "https://images.unsplash.com/photo-1500534623283-312aade485b7",
    "https://images.unsplash.com/photo-1470770841072-f978cf4d019e",
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "https://images.unsplash.com/photo-1462331940025-496dfbfc7564",
]

# Wallpaper URLs for mobile (16:9 portrait) - updated as per user feedback
mobile_wallpaper_urls = [
    "https://images.unsplash.com/photo-1604311795833-25e1d5c128c6?q=80&w=1527&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1581260466152-d2c0303e54f5?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8OSUzQTE2fGVufDB8fDB8fHww",
    "https://images.unsplash.com/photo-1566895291281-ea63efd4bdbc?q=80&w=1527&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
]

def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)

def download_and_save(url, folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        # Save image temporarily
        filename = os.path.basename(url.split("?")[0]) + ".jpg"
        save_path = os.path.join("wallpapers", filename)
        img.save(save_path)
        # Move to target folder
        shutil.move(save_path, os.path.join(folder, os.path.basename(save_path)))
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def main():
    clear_folder(mobile_folder)
    clear_folder(desktop_folder)

    for url in desktop_wallpaper_urls:
        download_and_save(url, desktop_folder)
    for url in mobile_wallpaper_urls:
        download_and_save(url, mobile_folder)

if __name__ == "__main__":
    main()
