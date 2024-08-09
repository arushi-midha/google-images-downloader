# Google Images Downloader

This Streamlit-based web application allows users to search and download images directly from Google Images. Users can specify a keyword and the number of images they want to download, and the app will handle the rest, saving the images to a local directory.

## How It Works

1. **Input**:
    - The user enters a keyword to search for images.
    - The user specifies the number of images to download (1-100).

2. **Search & Download**:
    - The app uses the Google Images Search API to find images matching the keyword.
    - The specified number of images are downloaded and saved to the `./images/` directory.

3. **Output**:
    - The app provides a success message once the images are downloaded.
    - The user can then check the `./images/` directory for the downloaded files.

## Interface
![image](https://github.com/user-attachments/assets/d30582da-0790-48af-85be-673a379e532b)


## Requirements

- Python 3.x
- Streamlit
- Google Images Search API key and CX (custom search engine)
- Google Images Search Python package (`google-images-search`)


## Developer

- **Arushi Midha** - [GitHub](https://github.com/arushi-midha)
