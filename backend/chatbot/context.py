file_path = "../data/resume_content.md"

with open(file_path, "r", encoding="utf-8") as file:
    parsed_resume = file.read()

def get_parsed_resume():
    return parsed_resume
