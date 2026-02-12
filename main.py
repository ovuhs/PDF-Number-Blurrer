import fitz  # PyMuPDF
import re
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageFilter
import io

def select_and_process_pdf():
    # Tkinter উইন্ডো হাইড করা
    root = tk.Tk()
    root.withdraw()

    print("Opening file dialog... Please select your PDF.")
    
    input_pdf_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not input_pdf_path:
        print("No file selected.")
        return

    # আউটপুট ফাইলের নাম জেনারেট করা
    file_dir, file_name = os.path.split(input_pdf_path)
    file_base, file_ext = os.path.splitext(file_name)
    output_pdf_path = os.path.join(file_dir, f"{file_base}_blurred_effect{file_ext}")

    try:
        doc = fitz.open(input_pdf_path)
        # সংখ্যা খোঁজার প্যাটার্ন
        number_pattern = re.compile(r'\d[\d,.]*[KM%]?')
        
        redacted_count = 0

        print("Processing pages (This may take a moment due to image processing)...")
        
        for page_num, page in enumerate(doc):
            words = page.get_text("words")
            
            # ব্লার করা ছবিগুলো এখানে জমা রাখা হবে
            images_to_insert = []
            
            for word in words:
                text = word[4]
                if number_pattern.search(text):
                    # ১. টেক্সটের এরিয়া সিলেক্ট করা
                    rect = fitz.Rect(word[0], word[1], word[2], word[3])
                    
                    # ২. ওই নির্দিষ্ট অংশের একটি হাই-কোয়ালিটি ছবি তোলা (Screenshot)
                    # matrix=fitz.Matrix(2, 2) রেজোলিউশন বাড়ায় যাতে ব্লার সুন্দর হয়
                    pix = page.get_pixmap(clip=rect, matrix=fitz.Matrix(2, 2))
                    
                    # ৩. ছবিটিকে PIL ফরম্যাটে কনভার্ট করা
                    img_data = pix.tobytes("png")
                    img = Image.open(io.BytesIO(img_data))
                    
                    # ৪. ছবিতে "Gaussian Blur" এফেক্ট দেওয়া
                    # radius=10 মানে কতটা ঘোলা হবে। কম-বেশি করতে পারেন।
                    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=3))
                    
                    # ৫. ব্লার করা ছবি মেমোরিতে সেভ করা
                    output_buffer = io.BytesIO()
                    blurred_img.save(output_buffer, format="PNG")
                    images_to_insert.append((rect, output_buffer.getvalue()))
                    
                    # ৬. আসল টেক্সট মুছে ফেলার জন্য মার্ক করা (সাদা রঙ দিয়ে)
                    # fill=(1, 1, 1) মানে সাদা। এতে কালো বক্স আসবে না।
                    page.add_redact_annot(rect, fill=(1, 1, 1))
                    redacted_count += 1

            # ৭. পেজ থেকে আসল টেক্সট মুছে ফেলা (সাদা হয়ে যাবে)
            page.apply_redactions()
            
            # ৮. সাদা জায়গার ওপর ব্লার করা ছবি বসিয়ে দেওয়া
            for rect, img_bytes in images_to_insert:
                page.insert_image(rect, stream=img_bytes)

            print(f"Page {page_num + 1} processed.")

        doc.save(output_pdf_path)
        print("-" * 30)
        print(f"DONE! Total {redacted_count} items blurred.")
        print(f"File saved: {output_pdf_path}")
        print("-" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    select_and_process_pdf()
