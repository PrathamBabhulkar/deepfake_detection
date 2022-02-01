# http://127.0.0.1:5000/
# https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/

import os
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from DeepFakeDetector.extract_landmarks import ExtractLandmarks
from DeepFakeDetector.classify import Classify


UPLOAD_FOLDER = 'D:\\arnav\\Python\\githubStuff\\deepfake-detector\\DeepFakeDetector\\input'
LANDMARKS_FOLDER = 'D:\\arnav\\Python\\githubStuff\\deepfake-detector\\DeepFakeDetector\\landmarks'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LANDMARKS_FOLDER'] = LANDMARKS_FOLDER
app.secret_key = "sdhwiuhdeiuwh"
# @app.route('/')
# def home():
#     return render_template("index.html")


# @app.route("/post/<int:blog_id>")
# def get_post(blog_id):
#     return render_template("post.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "<h1>Failed!</h1>"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "<h1>Select file!</h1>"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            video_filename = os.path.join(
                app.config['UPLOAD_FOLDER'], filename)
            landmark_filename = os.path.join(
                app.config['LANDMARKS_FOLDER'], f"{filename}.txt")
            file.save(video_filename)
            e = ExtractLandmarks()
            c = Classify()

            os.remove(video_filename)
            os.remove(landmark_filename)
            return f"<h1>{c.label}</h1>"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# 
# curl -X POST "http://127.0.0.1:5000/api" -F file=aagfhgtpmv.mp4
# curl -F file=@aagfhgtpmv.mp4 "http://127.0.0.1:5000/api"
@app.route('/api', methods=['POST'])
def upload_file_api():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return jsonify(
                success=False,
                message="No .mp4 video file sent."
            )

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "<h1>Select file!</h1>"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            video_filename = os.path.join(
                app.config['UPLOAD_FOLDER'], filename)
            landmark_filename = os.path.join(
                app.config['LANDMARKS_FOLDER'], f"{filename}.txt")
            file.save(video_filename)

            e = ExtractLandmarks()
            c = Classify()

            os.remove(video_filename)
            os.remove(landmark_filename)
            return jsonify(
                success=True,
                message=c.label
            )
    return jsonify(
        success=False,
        message="Unkown error, please send a video file as a post request."
    )


# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()

# @app.get('/shutdown')
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'


if __name__ == "__main__":
    app.run(debug=True)

# # start flask
# app = Flask(__name__)

# # render default webpage
# @app.route('/')
# def home():
#     return render_template('home.html')

# # when the post method detect, then redirect to success function
# @app.route('/', methods=['POST', 'GET'])
# def get_data():
#     if request.method == 'POST':
#         user = request.form['search']
#         return redirect(url_for('success', name=user))

# # get the data for the requested query
# @app.route('/success/<name>')
# def success(name):
#     return "<xmp>" + str(requestResults(name)) + " </xmp> "
