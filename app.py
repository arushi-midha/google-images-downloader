import streamlit as st
from google_images_search import GoogleImagesSearch

# Function to perform image search and download
def search_and_download_images(keyword, num_images):
    gis = GoogleImagesSearch('AIzaSyCGyqf36D5k3QghaZLhAqb1R2OUtRFraF8', '0d386b282da5209ea', validate_images=True)
    _search_params = {
        'q': keyword,
        'num': num_images,
        
    }

    # Path to directory where the downloaded images will be stored
    gis.search(search_params=_search_params, path_to_dir='./images/')
    return f'{num_images} images of {keyword} downloaded to ./images/'


st.title("Google Images Downloader")
st.write("Enter a keyword and the number of images you want to download.")

# Input fields for keyword and number of images
keyword = st.text_input("Keyword", value="motorbike")
num_images = st.number_input("Number of images", min_value=1, max_value=100, value=10, step=1)

# Button to trigger the image search
if st.button("Search and Download Images"):
    message = search_and_download_images(keyword, num_images)
    st.success(message)
    st.write("Check the './images/' directory for the downloaded images.")

footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: lavender;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: grey;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p> </p>
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/arushi-midha" target="_blank">Arushi Midha</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)