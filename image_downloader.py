import os
import requests

def download_image(url):
    # Try to download the image from the URL
    try:
        # Step 1: Fetch the image
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Step 2: Create the directory if it doesn't exist
            if not os.path.exists('Fetched_Images'):
                os.makedirs('Fetched_Images')

            # Step 3: Get the filename from the URL or create a default one
            filename = url.split('/')[-1]
            if not filename:
                filename = 'image.jpg'

            # Step 4: Save the image to the Fetched_Images folder
            with open(f'Fetched_Images/{filename}', 'wb') as file:
                file.write(response.content)

            print(f"Image saved as Fetched_Images/{filename}")
        else:
            print("Failed to retrieve the image. HTTP Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("There was an error with the request:", e)

# Step 5: Prompt the user for a URL
url = input("Enter the URL of the image: ")
download_image(url)
