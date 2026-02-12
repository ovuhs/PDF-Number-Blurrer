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
