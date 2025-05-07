import os
import pdfplumber
import re
import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from docx import Document

# Define common skills to match against
known_skills = [
    'Python', 'C++', 'Java', 'SQL', 'HTML', 'CSS', 'JavaScript',
    'Machine Learning', 'Data Analysis', 'React', 'Node.js', 'Django'
]

# Extract text from PDF pages
def extract_text_from_pdf(path):
    text = ''
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

# Extraction helpers
def extract_name(text):
    lines = text.strip().split('\n')
    return lines[0] if lines else "Not Found"

def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else "Not Found"

def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group() if match else "Not Found"

def extract_skills(text):
    return [skill for skill in known_skills if skill.lower() in text.lower()] or ["None Detected"]

def extract_projects(text):
    return '\n'.join([line for line in text.split('\n') if 'project' in line.lower()]) or "Not Found"

def extract_experience(text):
    keywords = ['experience', 'intern', 'worked at', 'internship']
    return '\n'.join([line for line in text.split('\n') if any(k in line.lower() for k in keywords)]) or "Not Found"

def extract_github(text):
    match = re.search(r'https?://github\.com/[^\s]+', text)
    return match.group() if match else "Not Found"

def extract_linkedin(text):
    match = re.search(r'https?://(www\.)?linkedin\.com/[^\s]+', text)
    return match.group() if match else "Not Found"

# Save extracted info as PDF
def save_as_pdf(info, path):
    c = canvas.Canvas(path)
    y = 800
    for line in info.split('\n'):
        c.drawString(50, y, line)
        y -= 20
    c.save()

# Save extracted info as Word DOCX
def save_as_docx(info, path):
    doc = Document()
    for line in info.split('\n'):
        doc.add_paragraph(line)
    doc.save(path)

# Browse and parse resume file
def browse_resume():
    filepath = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not filepath:
        return

    text = extract_text_from_pdf(filepath)
    print("DEBUG: Extracted Text:\n", text)

    if not text.strip():
        messagebox.showerror("Error", "No extractable text found in the PDF. It may be scanned or image-based.")
        return

    # Extract info
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    projects = extract_projects(text)
    experience = extract_experience(text)
    github = extract_github(text)
    linkedin = extract_linkedin(text)

    # Format result
    result = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Skills: {', '.join(skills)}\n\n"
        f"Experience:\n{experience}\n\n"
        f"Projects:\n{projects}\n\n"
        f"GitHub: {github}\n"
        f"LinkedIn: {linkedin}"
    )

    messagebox.showinfo("Resume Details", result)

    # Ask to save
    save_type = messagebox.askquestion("Download", "Do you want to save the extracted info?")
    if save_type == 'yes':
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF File", "*.pdf"), ("Word Doc", "*.docx")])
        if file_path.endswith('.pdf'):
            save_as_pdf(result, file_path)
        elif file_path.endswith('.docx'):
            save_as_docx(result, file_path)
        messagebox.showinfo("Saved", f"Details saved to: {file_path}")

# ---------- GUI ----------
root = tk.Tk()
root.title("Smart Resume Parser")
root.geometry("350x200")

label = tk.Label(root, text="Upload Resume (PDF)", font=('Arial', 12))
label.pack(pady=10)

btn = tk.Button(root, text="Browse Resume", command=browse_resume, bg="lightblue", font=('Arial', 11))
btn.pack(pady=10)

root.mainloop() 
