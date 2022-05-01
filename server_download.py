from flask import Flask, send_file, render_template, request, redirect
from subprocess import call
import os
import uuid
import shutil
from processor import imageGeneration

app = Flask(__name__)

working_dir = "./data/"

# Status
@app.route("/", methods=['GET', 'POST'])
def status():
    return 'Status: UP'

# Upload page, to uploader
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    return render_template('upload.html')

# Upload handler
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        incoming_data = request.get_json()

        path_in = r"{}".format(incoming_data['data']['path_in'])
        path_out = r"{}".format(incoming_data['data']['path_out'])
        path_arch = r"{}".format(incoming_data['data']['path_arch'])
        imageGeneration(path_in, path_out)
        shutil.make_archive(path_arch, 'zip', path_out)
        return path_in


# Download handler
@app.route("/download", methods=['GET', 'POST'])
def downloadFile():
    if request.method == 'POST':
        incoming_data = request.get_json()
        path_arch = r"{}".format(incoming_data['data']['path_arch'])
        return send_file(path_arch, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
