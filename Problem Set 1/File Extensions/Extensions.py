# extensions.py

def main():
    # Prompt the user for the name of a file
    file_name = input("Enter the name of a file: ").strip().lower()

    # Determine the media type based on the file extension
    media_type = get_media_type(file_name)

    # Output the media type
    print(media_type)

def get_media_type(file_name):
    # Define a dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Iterate over the dictionary to find the matching media type
    for extension, media_type in media_types.items():
        if file_name.endswith(extension):
            return media_type
    
    # If no matching extension is found, return the default media type
    return "application/octet-stream"

# Call the main function
if __name__ == "__main__":
    main()