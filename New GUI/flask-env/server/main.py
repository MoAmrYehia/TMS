from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from http_status import HttpStatus

from gensim.models import Word2Vec
import os
from pyresparser import ResumeParser
from werkzeug.utils import secure_filename

PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/pdfs')
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
CORS(app)

# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('index.html')

@app.route('/api/upload/', methods=['POST'])
def upload_and_predict():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))

    obj = data = ResumeParser(os.path.join(PARENT_DIR, f'server/static/pdfs/{filename}')).get_extracted_data()
    for k, v in obj.items():
        if not v:
            obj[k] = []
            
    return jsonify({"parsed_cv": obj}), HttpStatus.ok_200.value

@app.route('/api/predict/skills', methods=['POST'])
def predict_skills():
    model = Word2Vec.load(os.path.join(PARENT_DIR, 'server/model/trained_model_skills.bin'))
    w = request.form['skill']

    pred = model.most_similar(positive=[w], topn=10)

    return jsonify(pred), HttpStatus.ok_200.value
    
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)