# ✅ Updated scoring.py
def calculate_score(resume_data):
    score = 0
    feedback = []

    if resume_data['emails']:
        score += 1
    else:
        feedback.append("Missing email.")

    if resume_data['phones']:
        score += 1
    else:
        feedback.append("Missing phone number.")

    skill_count = len(resume_data['skills'])
    if skill_count:
        skill_score = min(skill_count / 5, 1.0) * 3
        score += skill_score
    else:
        feedback.append("No skills identified.")

    exp_count = len(resume_data['experience'])
    if exp_count:
        exp_score = min(exp_count / 5, 1.0) * 2
        score += exp_score
    else:
        feedback.append("No experience mentioned.")

    score += (resume_data['grammar_score'] / 10) * 2

    return {
        "total": round(score, 2),
        "feedback": feedback,
        "details": {
            "Email": bool(resume_data['emails']),
            "Phone": bool(resume_data['phones']),
            "Skills Found": skill_count,
            "Experience Entries": exp_count,
            "Grammar Score": resume_data['grammar_score']
        }
    }

