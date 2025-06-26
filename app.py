from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    filename = 'comic_database.zip'
    return send_from_directory(directory=os.path.join(app.root_path, 'static'), path=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True) 