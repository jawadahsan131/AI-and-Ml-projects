import fitz
import re
import spacy
from textblob import TextBlob

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined Skills List
known_skills = [
    'project management', 'risk management', 'system optimization',
    'vendor relations', 'mechanical systems', 'quality control',
    'data analysis', 'prototyping', 'manufacturing', 'design', 'testing'
]

def extract_resume_info(pdf_path):
    doc = fitz.open(pdf_path)
    text = " ".join([page.get_text() for page in doc])

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    phones = re.findall(r'\+?\d[\d\s\-\(\)]{8,}\d', text)

    doc_nlp = nlp(text)

    skill_tokens = set([token.text.lower() for token in doc_nlp])
    skills = [skill.title() for skill in known_skills if any(word in skill_tokens for word in skill.lower().split())]

    experience_labels = ["ORG", "PRODUCT", "EVENT", "PERSON", "GPE"]
    experience = [ent.text for ent in doc_nlp.ents if ent.label_ in experience_labels]
    experience = sorted(set(experience))

    blob = TextBlob(text)
    grammar_errors = sum(1 for sentence in blob.sentences if sentence.correct() != sentence)
    grammar_score = max(0, 10 - grammar_errors)

    return {
        "emails": list(set(emails)),
        "phones": list(set(phones)),
        "skills": sorted(set(skills)),
        "experience": experience,
        "grammar_score": grammar_score,
        "raw_text": text
    }

def split_resume_sections(text):
    sections = {"experience": "", "education": "", "certificates": ""}
    current_section = None

    for line in text.splitlines():
        line_clean = line.strip().lower()
        if 'experience' in line_clean:
            current_section = "experience"
        elif 'education' in line_clean:
            current_section = "education"
        elif 'certificate' in line_clean or 'certifications' in line_clean:
            current_section = "certificates"
        elif current_section:
            sections[current_section] += line.strip() + " "

    return sections
