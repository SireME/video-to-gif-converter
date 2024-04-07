from flask import Flask, request, render_template, send_file, jsonify
from flask import redirect, url_for
from videotogif import convert_to_gif
import os
import tempfile
import uuid
import threading

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER


def delete_uploaded_file(file_path):
    os.remove(file_path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        # Generate a UUID for the file name
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(video_path)
        
        # Start a thread to delete the uploaded file after 10 minutes
        delete_thread = threading.Timer(600, delete_uploaded_file, args=[video_path])
        delete_thread.start()
        
        gif_name = os.path.splitext(filename)[0] + '.gif'
        gif_path = os.path.join(app.config['CONVERTED_FOLDER'], gif_name)
        
        convert_to_gif(video_path, gif_path)
        
        # Construct the download URL for the converted GIF
        download_url = url_for('download', filename=gif_name)
        
        # Return a redirect response to the download route
        return redirect(download_url)

@app.route('/download/<filename>')
def download(filename):
    return render_template('download.html', filename=filename)

@app.route('/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['CONVERTED_FOLDER'], filename), as_attachment=True)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['CONVERTED_FOLDER'], exist_ok=True)
    app.run(debug=True)
