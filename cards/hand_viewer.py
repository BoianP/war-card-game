import tkinter as tk
from PIL import Image, ImageTk
from .card import Card, Suit
from .pile import Pile

directory = os.path.join(os.getcwd(), "card images") 

def show_card_window(c: Card):
    win = tk.Toplevel()
    win.title("Card")
    win.geometry("170x200")

    card_file = f"{Card.rank_names[c.rank]}_of_{c.suit.display_name}.png"
    full_path = os.path.join(directory, card_file)

    if not os.path.isfile(full_path):
        tk.Label(win, text="Image not found", fg="red").pack(pady=20)
    else:
        img = Image.open(full_path)
        tk_img = ImageTk.PhotoImage(img)
        label = tk.Label(win, image=tk_img)
        label.pack(pady=5)
        win.image = tk_img
        
def show_hand_window(cards: list[Card]):
    window = tk.Tk()
    window.title("Your Hand")
    window.geometry("600x300")

    title_label = tk.Label(window, text="Your Cards by Suit:", font=("Helvetica", 16))
    title_label.pack(anchor="w", padx=10, pady=(10, 5))

    # Organize cards by suit
    suit_rows = Pile(cards).group_by_suit()

    # For each suit, create a row (a Frame) and add cards as buttons
    for suit in Suit:
        row_frame = tk.Frame(window)
        row_frame.pack(anchor="w", padx=20, pady=4)

        suit_label = tk.Label(row_frame, text=str(suit), font=("Courier", 14))
        suit_label.pack(side="left", padx=(0, 10))

        for card in sorted(suit_rows[suit]):
            btn = tk.Button(row_frame, text=card.short_symbol(), font=("Courier", 14),
                            command=lambda c=card: show_card_window(c))
            btn.pack(side="left", padx=5)

    window.mainloop()

if __name__ == "__main__":
    test_hand = [
        Card(1, Suit.SPADES),
        Card(11, Suit.HEARTS),
        Card(10, Suit.DIAMONDS),
        Card(7, Suit.CLUBS),
        Card(2, Suit.HEARTS),
        Card(5, Suit.SPADES),
    ]
    show_hand_window(test_hand)

