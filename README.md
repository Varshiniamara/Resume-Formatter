# 📄 Smart Resume Parser

A Python-based GUI application that extracts key information from PDF resumes like **name, email, phone number, skills, experience, projects, GitHub, and LinkedIn links**, and allows users to **save the extracted data as PDF or Word documents**.

---

## 🚀 Features

- 📄 Extracts text from PDF resumes
- 🔍 Automatically detects:
  - Name
  - Email address
  - Phone number
  - Skills (from a predefined list)
  - Work experience
  - Project mentions
  - GitHub & LinkedIn profile URLs
- 💾 Save extracted details as:
  - PDF (`.pdf`)
  - Word Document (`.docx`)
- 🖥️ User-friendly GUI using `Tkinter`

---

## 🧰 Tech Stack

- `Python 3.x`
- `pdfplumber` – for extracting text from PDFs
- `re` – for regular expression-based parsing
- `tkinter` – for GUI
- `reportlab` – for saving data as PDF
- `python-docx` – for saving data as Word DOCX

---

## 📦 Requirements

Install required packages using pip:

```bash
pip install pdfplumber reportlab python-docx
