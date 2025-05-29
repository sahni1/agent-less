import os

def count_media_in_folder(folder_path):
    # Define common image and video extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']

    # Initialize counters for images and videos
    image_count = 0
    video_count = 0

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Get the file extension
            ext = os.path.splitext(file)[1].lower()

            # Check if the file is an image
            if ext in image_extensions:
                image_count += 1
            # Check if the file is a video
            elif ext in video_extensions:
                video_count += 1

    return image_count, video_count

# Example usage
folder_path = r'F:\sahil\Pictures\.thumbnails'  # Raw string to avoid escape issues
images, videos = count_media_in_folder(folder_path)
print(f"Total number of images: {images}")
print(f"Total number of videos: {videos}")
