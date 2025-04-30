from flask import Flask, send_from_directory, jsonify, render_template
import os
import subprocess
import threading

app = Flask(__name__)

# Folder paths
mobile_folder = "wallpapers/wallpapers_for_mobile"
desktop_folder = "wallpapers/wallpapers_for_desktops"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wallpapers/mobile/<filename>')
def mobile_wallpapers(filename):
    return send_from_directory(mobile_folder, filename)

@app.route('/wallpapers/desktop/<filename>')
def desktop_wallpapers(filename):
    return send_from_directory(desktop_folder, filename)

@app.route('/api/wallpapers/mobile')
def list_mobile_wallpapers():
    files = os.listdir(mobile_folder)
    return jsonify(files)

@app.route('/api/wallpapers/desktop')
def list_desktop_wallpapers():
    files = os.listdir(desktop_folder)
    return jsonify(files)

@app.route('/api/refresh', methods=['POST'])
def refresh_wallpapers():
    def run_script():
        subprocess.run(["python3", "download_wallpapers.py"])
    thread = threading.Thread(target=run_script)
    thread.start()
    return jsonify({"status": "refresh started"})

if __name__ == '__main__':
    app.run(debug=True)
