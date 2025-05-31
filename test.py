from PIL import Image, ImageTk
import os

import tkinter as tk
from cards.card import Card, Suit
from cards.pile import Pile

def show_card_window(card: Card):
    win = tk.Toplevel()
    win.title("Card Detail")
    win.geometry("200x100")

    label = tk.Label(win, text=str(card), font=("Helvetica", 20))
    label.pack(pady=20)

cwd = os.getcwd()

root = tk.Tk()
root.withdraw()

img = Image.open(os.path.join("card images","10_of_clubs.svg.png"))
tk_img = ImageTk.PhotoImage(img)



win = tk.Toplevel(root)
win.title("Card Detail")
win.geometry("170x200")
label = tk.Label(win, image=tk_img)
label.pack(pady=5)

win.image = tk_img

#win.mainloop()
# This ensures the app fully closes when you close the card window
win.protocol("WM_DELETE_WINDOW", root.quit)

root.mainloop()