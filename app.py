from flask import Flask, request, render_template, send_file
from moviepy.editor import VideoFileClip
import os
import tempfile
from videotogif import convert_to_gif

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER



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
        filename = file.filename
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(video_path)
        
        gif_name = os.path.splitext(filename)[0] + '.gif'
        gif_path = os.path.join(app.config['CONVERTED_FOLDER'], gif_name)
        
        convert_to_gif(video_path, gif_path)
        
        return jsonify({'status': 'success', 'gif_name': gif_name})


@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['CONVERTED_FOLDER'], filename), as_attachment=True)


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['CONVERTED_FOLDER'], exist_ok=True)
    app.run(debug=True)
