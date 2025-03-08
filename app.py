from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from model import rank_resumes

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload():
    if 'job_desc' not in request.form:
        return jsonify({"error": "Job description is required"}), 400

    job_desc = request.form['job_desc']
    resume_files = request.files.getlist('resumes')

    if not resume_files:
        return jsonify({"error": "No resumes uploaded"}), 400

    resume_paths = []
    for file in resume_files:
        if file.filename == "":
            continue  # Skip empty files

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        resume_paths.append(filepath)

    if not resume_paths:
        return jsonify({"error": "No valid resumes uploaded"}), 400

    try:
        ranked_resumes = rank_resumes(resume_paths, job_desc)
        response = [{"resume": os.path.basename(res), "score": score[0]} for res, score in ranked_resumes]
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
