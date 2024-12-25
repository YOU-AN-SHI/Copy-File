from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    destination = request.form['destination']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not destination:
        return jsonify({'error': 'No destination provided'}), 400

    try:
        destination_path = os.path.join(destination, file.filename)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)  # 確保目錄存在
        file.save(destination_path)
        return jsonify({'message': 'File successfully copied'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)