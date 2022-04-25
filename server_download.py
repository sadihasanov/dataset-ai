from flask import Flask, send_file, render_template, request, redirect
from subprocess import call
import os
import uuid
import shutil

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
        global uid
        global path_in
        global path_out
        global path_arch
        f = request.files.getlist("file")
        uid = str(uuid.uuid4())
        path_in = os.path.join(working_dir + "in/", uid)
        path_out = os.path.join(working_dir + "out/")
        path_arch = os.path.join(working_dir + "arch/", uid)
        os.mkdir(path_in)
        for file in f:
            file.save(os.path.join(path_in, file.filename))
        print("Files has been uploaded")
        call(["python", "./processor.py"])
        shutil.make_archive(path_arch, 'zip', path_out)
        #files_rem = glob.glob(path_out+"*")
        #for f in files_rem:
        #    os.remove(f)
        return redirect('upload')

# Download handler
@app.route("/download")
def downloadFile():
    archive = path_arch + ".zip"
    return send_file(archive, as_attachment=True)


if __name__ == "__main__":
    app.run(debug = True)
