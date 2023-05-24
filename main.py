from tkinter import filedialog
from PIL import Image
from sys import exit

original_name = filedialog.askopenfilename(
    initialdir="/",
    title="Select image file",
    filetypes=(
        ("png files", "*.png"),
        ("jpg files", "*.jpg"),
        ("jpeg files", "*.jpeg"),
        ("webp files", "*.webp"),
        ("all files", "*.*")
    )
)
print(original_name)

if original_name == "":
    exit()

converted_name = original_name[0:original_name.rfind('.')] + ".ico"
logo = Image.open(original_name)
logo.save(converted_name, format='ICO')

# pyinstaller -wF main.py
