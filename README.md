# Image Downloader Script

This Python script downloads an image from a provided URL and saves it in a folder called `Fetched_Images`. It handles errors gracefully and checks if the image URL is valid before downloading.

## Features

- Prompts the user to enter an image URL.
- Creates a folder called `Fetched_Images` if it doesn't already exist.
- Downloads the image and saves it in the `Fetched_Images` folder.
- Handles errors such as network issues or invalid URLs.

## Requirements

You need Python 3 and the `requests` library installed. You can install the `requests` library using the following command:
pip install requests

## How to Use

1. Clone or download the repository to your local machine.
2. Open the terminal or command prompt and navigate to the folder where the script is located.
3. Run the script by typing: 
   python image_downloader.py
4. When prompted, paste the URL of the image you want to download.
5. The image will be saved in a folder called `Fetched_Images` in the same directory.

## Example

Enter the URL of the image: https://example.com/path/to/image.jpg
Image saved as Fetched_Images/image.jpg


If there is an error, such as an invalid URL or network issue, the script will display an error message.

## Notes

- The image is saved with its original filename if possible, or a default name (`image.jpg`) will be used.
- The script checks if the `Fetched_Images` folder exists and creates it if necessary.
- It only downloads images, so URLs that point to other resources may not work.

## License

Feel free to use or modify this code as you like! No formal license, just credit the original idea if you share it.
