# PDF Number Blurrer

A Python automation tool that scans PDF documents, detects numerical values (e.g., financial figures, phone numbers), and applies a visual "Gaussian Blur" effect to them while maintaining the original document layout.

This is useful for sharing documents where sensitive numerical data needs to be obscured but the overall structure must remain visible.

## 🚀 Features

- **Automated Detection:** Uses Regex to find numbers, currency, and percentages (e.g., `1,000`, `50%`, `10.5M`).
- **Visual Redaction:** Instead of blacking out text, it takes a high-quality screenshot of the number and applies a professional blur effect.
- **Privacy Focused:** The original text underneath the blur is physically removed (redacted) from the PDF layer to prevent copy-pasting.
- **GUI Selection:** Simple pop-up window to select files easily.

## 🛠️ Prerequisites

Make sure you have Python installed. This project relies on the following libraries:
- `PyMuPDF` (fitz) for PDF processing.
- `Pillow` (PIL) for image manipulation.
- `tkinter` (Standard with Python) for the file dialog.

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/ovuhs/PDF-Number-Blurrer.git](https://github.com/ovuhs/PDF-Number-Blurrer.git)
   cd PDF-Number-Blurrer

2. Install the required dependencies:
```bash
pip install -r requirements.txt
					
3. 💻 Usage
Run the script:
```bash
python main.py

(Note: Replace main.py with whatever you named your script)

4. A file dialog window will appear. Select the PDF file you want to process.
The script will generate a new file in the same directory named filename_blurred_effect.pdf.

5. ⚙️ How It Works
      1. Scan: The script iterates through every word in the PDF using PyMuPDF.
      2. Match: It checks if the text matches the number pattern (Regex).
      3. Capture: It takes a high-resolution snapshot of that specific area.
      4. Blur: It applies a Gaussian Blur filter using Pillow.
      5. Redact & Replace: It removes the underlying text (making it unreadable/unsearchable) and inserts the blurred image in its exact position.

6. 📝 License
This project is open-source and available for personal and educational use.
