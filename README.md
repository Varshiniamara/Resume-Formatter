# 📄 Smart Resume Parser — AI-Driven Portfolio Insight Tool

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Project-success.svg)](#)

A high-performance Python desktop application that leverages **Regex-driven analysis** and **PDF text extraction** to transform unstructured resume data into structured insights. Designed for high efficiency, it extracts contact information, identified skills, project history, and experience details in seconds.

---

## 📸 Desktop Interface Breakdown
![Smart Resume Parser GUI](assets/gui_mockup.png)

---

## 🚀 Key Features

- **🧠 Smart Extraction Engine**: Automatically identifies key entities including:
  - **Personal Details**: Name, Email, and Phone.
  - **Technical DNA**: Matching skills against a curated list (Python, ML, React, etc.).
  - **Professional footprint**: Extracts work experience and project mentions.
  - **Social Identities**: Direct deep-linking to GitHub and LinkedIn profiles.
- **📄 PDF-to-Text Processing**: Utilizes `pdfplumber` for high-fidelity text extraction.
- **💾 Multi-Format Export**: Seamlessly save parsed results as professional **PDF** or **Word (.docx)** documents.
- **🖥️ Responsive GUI**: Lightweight, modern interface built on `Tkinter`.

---

## 🧰 Technology Architecture

### **Core Stack**
- **Python 3.x**: The engine powering the logic.
- **pdfplumber**: Used for reading and mining PDF document data.
- **Regex (re)**: The backbone of the named entity extraction logic.

### **Export & GUI**
- **Tkinter**: Provides the standard desktop user experience.
- **ReportLab**: Generates real-time PDF summaries of the parsed data.
- **Python-docx**: Automates the creation of MS Word counterparts.

---

## 📦 Local Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Varshiniamara/Resume-Formatter.git
   cd Resume-Formatter
   ```

2. **Install Dependencies**:
   ```bash
   pip install pdfplumber reportlab python-docx
   ```

3. **Launch the Application**:
   ```bash
   python code.py
   ```

---

## 📂 Project Structure
```text
Resume-Formatter/
├── assets/           # UI Mockups & Visual Assets
├── code.py           # Main logic & GUI implementation
├── README.md         # Documentation & Feature Breakdown
```

---

## 📜 Usage Workflow
1. **Upload**: Launch the app and click "Browse Resume" to select a PDF.
2. **Analysis**: The script parses the text using Regex patterns and internal dictionaries.
3. **Review**: View the extracted summary in the real-time popup.
4. **Export**: Choose your preferred format (.pdf or .docx) to save the structured data for further use.

---

## 🏗️ Technical Implementation Note
The parser uses a **Keyword-Matching Strategy** combined with **Pattern-Based Recognition** (Regex) for social links and contact info. This approach ensures high speed while maintaining accuracy for standard resume formats.
