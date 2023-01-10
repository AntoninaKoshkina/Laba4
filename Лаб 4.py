import tkinter as tk
import pygame
from tkinter import *
from PIL import ImageTk, Image
from key import key
from itertools import count


root = Tk()
pygame.mixer.init()
root.title("Slime Rancher")
root.geometry("1920x1080")


class ImageLabel(tk.Label):

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def play():
    pygame.mixer.music.load("муз.mp3")
    pygame.mixer.music.play(-1)


def clicked():
    lbl_result.configure(text=key())


lbl = ImageLabel(root)
lbl.pack()

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

bg = tk.PhotoImage(lbl.load('гиф.gif'))
label_bg = tk.Label(frame, image=bg)
label_bg.place(x=0, y=0)

lbl_result = tk.Label(frame, font=("Arial", 25))
lbl_result.grid(column=0, row=0, padx=10, pady=10)

btn = tk.Button(frame, text='Сгенерировать ключ', font=("Arial", 25), command=clicked)
btn.grid(column=0, row=3)

play()

root.mainloop()
