from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from werkzeug import secure_filename
import base64

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['img_data']=''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            encoded = base64.b64encode(file.read())
            mime = "image/jpg"
            mime = mime + ";" if mime else ";"
            app.config['img_data'] = app.config['img_data'] + "data:%sbase64,%s" % (mime, encoded)
            return redirect(url_for("uploaded_file",filename=filename))
    return

@app.route('/show/<filename>')
def uploaded_file(filename):
     return render_template('template.html',input_image=app.config['img_data'])

if __name__ == '__main__':
    app.run()