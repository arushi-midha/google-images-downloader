from flask import Flask, render_template, request, send_file, redirect, url_for
from downloader import search_and_download_images
import os
import zipfile
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_images', methods=['POST'])
def download_images():
    keyword = request.form.get('keyword')
    num_images = int(request.form.get('num_images'))
    email = request.form.get('email')

    # Run the downloader
    result_message = search_and_download_images(keyword, num_images)
    
    # Zip the downloaded images
    zip_file_path = "./static/images.zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, dirs, files in os.walk('./static/images'):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), './static/images'))
    
    # Send the zip file via email
    if email:
        try:
            send_email_with_attachment(email, zip_file_path)
            return f"Images downloaded and sent to {email}."
        except Exception as e:
            return f"Failed to send email: {e}"
    else:
        return "No email provided."

def send_email_with_attachment(recipient_email, file_path):
    # Create email message
    msg = EmailMessage()
    msg['Subject'] = "Your Downloaded Images"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg.set_content("Here are your downloaded images!")

    # Attach the zip file
    with open(file_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='zip', filename="images.zip")

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    os.makedirs('./static/images', exist_ok=True)
    app.run(debug=True)
