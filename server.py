from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Directory where .txt files are stored
TXT_FOLDER = 'shared'

# Ensure the directory exists
os.makedirs(TXT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return "Welcome to the TXT File Server. Use /download/<filename> to get a file."

@app.route('/download/<filename>')
def download_file(filename):
    # Security check: serve only .txt files
    if not filename.endswith('.txt'):
        abort(403, description="Only .txt files are allowed.")
    
    try:
        return send_from_directory(TXT_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, description="File not found.")

if __name__ == '__main__':
    # Use host='0.0.0.0' to make it globally accessible (on your public IP or network)
    # Use port=5000 or any other port you like
    app.run(host='0.0.0.0', port=5000, debug=True)
