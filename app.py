from flask import Flask, render_template, request, send_file
from downloader import search_and_download_images
import os
import zipfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_images', methods=['POST'])
def download_images():
    keyword = request.form.get('keyword')
    num_images = int(request.form.get('num_images'))
    
    # Run the downloader
    result_message = search_and_download_images(keyword, num_images)
    
    # Zip the downloaded images to send as a single file
    zip_file_path = "./static/images.zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, dirs, files in os.walk('./static/images'):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), './static/images'))
    
    return send_file(zip_file_path, as_attachment=True)

if __name__ == "__main__":
    # Create the images directory if it doesn't exist
    os.makedirs('./static/images', exist_ok=True)
    app.run(debug=True)
