# http://127.0.0.1:5000/
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


# @app.route("/post/<int:blog_id>")
# def get_post(blog_id):
#     return render_template("post.html")


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