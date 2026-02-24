import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

URL = "https://cataas.com/cat"

class CatGenerator:

    def __init__(self, root, url=URL):
        self.root = root
        self.root.title("Генератор котов")
        self.root.geometry("500x500")
        self.url = url
        self.label = tk.Label(root)
        self.label.pack(pady=10)

        self.button = tk.Button(
            root,
            text="Следующая картинка",
            command=self.load_cat,
            font=("Arial", 14)
        )
        self.button.pack(pady=10)
        self.load_cat()

    def load_cat(self):

        try:
            response = requests.get(self.url)
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image = image.resize((400, 400))
            self.photo = ImageTk.PhotoImage(image)
            self.label.config(image=self.photo)

        except Exception as e:
            print("Ошибка загрузки:", e)


if __name__ == "__main__":
    root = tk.Tk()
    app = CatGenerator(root)
    root.mainloop()