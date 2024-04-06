# Video to GIF Converter

This project is a web application built with Flask that allows users to upload a video file, randomly extract a 20-second segment from it, convert that segment to a GIF, and provide a download link for the converted GIF.

## Features

- User-friendly web interface for uploading video files.
- Randomly extracts a 20-second segment from the uploaded video.
- Converts the extracted segment to a GIF.
- Provides a download link for the converted GIF.

## Requirements

- Python 3.x
- Flask
- MoviePy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/video-to-gif-converter.git
    ```

2. Navigate to the project directory:

    ```bash
    cd video-to-gif-converter
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open a web browser and go to [http://localhost:5000](http://localhost:5000).
   
3. Upload a video file using the provided form.

4. Click the "Convert" button to initiate the conversion process.

5. Once the conversion is complete, a download link for the GIF will be provided.

## Project Structure

    video-to-gif-converter/
    │
    ├── app.py # Main Flask application file
    ├── templates/ # HTML templates
    │ ├── index.html # Main upload page template
    │ └── download.html # Template for the download page
    ├── uploads/ # Folder to store uploaded video files
    ├── converted/ # Folder to store converted GIF files
    ├── static/ # Static assets (e.g., CSS, JavaScript)
    │ └── style.css # CSS styles
    └── requirements.txt # Python dependencies  


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by [MoviePy](https://github.com/Zulko/moviepy).

