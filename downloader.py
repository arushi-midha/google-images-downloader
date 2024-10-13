from google_images_search import GoogleImagesSearch
import os

def search_and_download_images(keyword, num_images):
    # Initialize GoogleImagesSearch
    gis = GoogleImagesSearch('AIzaSyCGyqf36D5k3QghaZLhAqb1R2OUtRFraF8', '0d386b282da5209ea')

    # Define search parameters
    search_params = {
        'q': keyword,
        'num': num_images,
        'safe': 'high',  # High safety level
    }

    # Path to save downloaded images
    path_to_images = './static/images/'
    
    # Clear any existing images in the folder
    for f in os.listdir(path_to_images):
        os.remove(os.path.join(path_to_images, f))

    # Execute search and download
    gis.search(search_params=search_params, path_to_dir=path_to_images)
    return f'{num_images} images of "{keyword}" downloaded to {path_to_images}'
