from flask import Flask, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdfFile' not in request.files:
        return 'No file part', 400

    pdf_file = request.files['pdfFile']
    pdf_file.save('pdf/sample.pdf')  # Change the path to your desired location
    return 'PDF uploaded successfully', 200

if __name__ == '__main__':
    app.run()
