import os

def rename_images(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only image files (you can customize this based on your image file extensions)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Sort the image files
    image_files.sort()
    
    # Rename the files numerically
    for i, old_name in enumerate(image_files):
        # Get the file extension
        _, extension = os.path.splitext(old_name)
        new_name = f"{i + 1}{extension}"  # Keep the original file extension
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")

# Replace 'C:\\Users\\offic\\Pictures\\New us' with the actual path to your folder containing images
folder_path = 'C:\\Users\\offic\\Pictures\\New us'

# Call the function to rename images
rename_images(folder_path)
