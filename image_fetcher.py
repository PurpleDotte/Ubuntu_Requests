import os
import requests
from urllib.parse import urlparse
import hashlib

def download_image(url):
    try:
        # Send a GET request to the image URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if the request was successful

        # Check if the content is an image
        if 'image' not in response.headers.get('Content-Type', ''):
            print(f"✗ {url} is not an image. Skipping...")
            return
        
        # Create the "Fetched_Images" directory if it doesn't exist
        if not os.path.exists("Fetched_Images"):
            os.makedirs("Fetched_Images")
        
        # Get the filename from the URL or use a default name
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Create a path for the image
        filepath = os.path.join("Fetched_Images", filename)
        
        # Check if the image already exists (to prevent duplicates)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                existing_image = f.read()
                # If the content is the same, skip saving it
                if hashlib.md5(existing_image).hexdigest() == hashlib.md5(response.content).hexdigest():
                    print(f"✗ Duplicate image found: {filename}. Skipping...")
                    return
        
        # Save the image to the Fetched_Images folder
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✓ Successfully fetched and saved: {filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URLs from the user (can be a single or multiple URLs)
    urls = input("Enter image URLs (separate by commas): ").split(',')
    
    # Process each URL one by one
    for url in urls:
        url = url.strip()  # Remove any extra spaces
        download_image(url)
    
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
