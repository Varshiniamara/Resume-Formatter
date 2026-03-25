# Smart Resume Parser

A simple Python-based GUI application to extract basic information from PDF resumes. It helps in parsing contact details, skills, and experience, and allows saving the results as a PDF or Word document.

## Features
- Extracts Name, Email, and Phone number.
- Identifies skills (Python, C++, Java, etc.).
- Extracts mentioned projects and experience.
- Detects GitHub and LinkedIn links.
- Saves output as `.pdf` or `.docx`.

## Tech Stack
- **Language**: Python
- **Libraries**: pdfplumber, tkinter, reportlab, python-docx

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Varshiniamara/Resume-Formatter.git
   ```
2. Install dependencies:
   ```bash
   pip install pdfplumber reportlab python-docx
   ```
3. Run the application:
   ```bash
   python code.py
   ```

## Folder Structure
- `code.py`: Main Python script.
- `README.md`: Project documentation.
