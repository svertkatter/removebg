import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from rembg import remove

def remove_background(input_path, output_path):
    image_input = Image.open(input_path)
    output = remove(image_input)
    output.save(output_path)
    return output_path

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        output_path = 'output.png'  # 出力ファイル名は必要に応じて変更してください
        remove_background(file_path, output_path)
        img = Image.open(output_path)
        img.thumbnail((350, 350))  # ウィンドウに収まるようにサイズを調整
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(window, image=img)
        panel.image = img
        panel.pack()

window = tk.Tk()
window.title('背景削除アプリ')

button = tk.Button(window, text='画像を開く', command=load_image)
button.pack()

window.mainloop()
