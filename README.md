# Ubuntu Image Fetcher

Welcome to the Ubuntu Image Fetcher! This Python tool helps you download images from the web and saves them in a folder called `Fetched_Images`. You can even handle multiple URLs at once and avoid downloading duplicate images.

## Features

- Download images from URLs provided by the user.
- Create a folder called `Fetched_Images` to store the images.
- Skip downloading duplicate images if they've already been saved.
- Handles basic errors like network issues or invalid URLs.

## Requirements

You need Python 3 and the `requests` library to use this script. If you don't have `requests` installed, you can install it using pip:

pip install requests


## How to Use

1. Download or clone this repository to your computer.
2. Open a terminal or command prompt and navigate to the folder where the script is located.
3. Run the script with:

python image_fetcher.py


4. When prompted, enter the image URLs you want to download. You can enter multiple URLs, separated 
   by commas.
5. The script will download the images and save them to a folder called `Fetched_Images`.

### Example

Enter image URLs (separate by commas): https://example.com/ubuntu-wallpaper.jpg
https://example.com/another-image.png

✓ Successfully fetched and saved: ubuntu-wallpaper.jpg
✓ Successfully fetched and saved: another-image.png


If you try to download the same image again, it will be skipped to avoid duplicates:

Enter image URLs (separate by commas): https://example.com/ubuntu-wallpaper.jpg
https://example.com/ubuntu-wallpaper.jpg

✓ Successfully fetched and saved: ubuntu-wallpaper.jpg
✗ Duplicate image found: ubuntu-wallpaper.jpg. Skipping...


## Notes

- The images are saved in the `Fetched_Images` folder in the same directory as the script.
- If the URL doesn’t point to an image, it will be skipped.
- If an image is already downloaded, it won’t be downloaded again.

## License

Feel free to use this tool however you like! No special license—just give credit if you share it.
