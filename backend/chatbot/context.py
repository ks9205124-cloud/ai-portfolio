from pathlib import Path

# Automatically finds 'data/resume_content.md' relative to the project root
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "resume_content.md"

with open(file_path, "r", encoding="utf-8") as file:
    parsed_resume = file.read()

def get_parsed_resume():
    return parsed_resume