from flask import Flask, request, jsonify
from google_images_search import GoogleImagesSearch

app = Flask(__name__)

# Initialize Google Images Search API
gis = GoogleImagesSearch('AIzaSyCGyqf36D5k3QghaZLhAqb1R2OUtRFraF8', '0d386b282da5209ea')

@app.route('/download-images', methods=['POST'])
def download_images():
    data = request.json
    keyword = data['keyword']
    num_images = data['num_images']

    try:
        # Set search parameters
        search_params = {
            'q': keyword,
            'num': num_images
        }
        
        # Download images to './images/' directory
        gis.search(search_params=search_params, path_to_dir='./images/')
        message = f"{num_images} images of '{keyword}' downloaded to ./images/."
        
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"message": f"Error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
