from transformers import pipeline, Pipeline
import random

# 🛠 Load a small instruction-following model
try:
    resume_improver: Pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        tokenizer="google/flan-t5-small"
    )
except Exception as e:
    resume_improver = None
    print(f"Error loading model: {e}")

def improve_resume_section(text, section_name="Overall"):
    """
    Takes a resume section and returns improved professional suggestions.
    """
    if resume_improver is None:
        return ["Error: Resume improvement model not loaded."]

    # Limit text to reasonable length (first 300 words)
    short_text = ' '.join(text.strip().split()[:300])
    
    prompt = f"Improve the following resume {section_name.lower()} section to make it more professional and impactful:\n\n{short_text}"

    try:
        output = resume_improver(
            prompt,
            max_length=256,
            temperature=0.7,
            top_p=0.95,
            do_sample=True,
        )
        return [output[0]['generated_text'].strip()]
    except Exception as e:
        return [f"Error generating suggestion: {e}"]
