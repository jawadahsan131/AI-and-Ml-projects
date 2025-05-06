from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from models.nlp_extract import extract_resume_info, split_resume_sections
from utils.scoring import calculate_score
from ai.gpt_suggestions import improve_resume_section

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['resume']
        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            resume_data = extract_resume_info(filepath)
            scorecard = calculate_score(resume_data)
            sections = split_resume_sections(resume_data['raw_text'])

            ai_suggestions = {}
            for section, text in sections.items():
                improved = improve_resume_section(text, section_name=section)
                ai_suggestions[section.title()] = improved

            result = {
                "Resume Data": resume_data,
                "Scorecard": scorecard,
                "Suggestions": ai_suggestions
            }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
