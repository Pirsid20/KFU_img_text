import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image and PDF files", "*.png *.jpg *.pdf")])
    return file_path

def get_text(file_path, lang):
    if file_path.endswith('.pdf'):
        images = convert_from_path(file_path)
        text = ''
        for image in images:
            text += pytesseract.image_to_string(image, lang=lang)
    else:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image, lang=lang)
    return text

def display_text(text):
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, text)

def process_file():
    file_path = load_file()
    text = get_text(file_path, language.get())
    display_text(text)

root = tk.Tk()

load_button = tk.Button(root, text="Загрузить", command=process_file)
load_button.pack()

language = tk.StringVar(root)
language.set("rus")  # default value

lang_button = tk.OptionMenu(root, language, "rus", "eng", "fra", "deu")
lang_button.pack()

text_area = tk.Text(root)
text_area.pack()

root.mainloop()

