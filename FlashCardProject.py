from tkinter import *
import random as rd
import pandas as pd

data = pd.read_csv(r"C:\Users\rahul\Downloads\words.csv")
data100 = data[0:101]
russian = data100.to_dict(orient="records")

# CONSTANTS
BACKGROUND = "#60A2B2"
POINTS = 0
curr = {}
ATTEMPTED = 0


def next_card():
    global curr, flip_timer, ATTEMPTED
    curr = rd.choice(russian)
    windows.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=curr["Russian"], fill="black")
    canvas.itemconfig(front, image=card_front)
    canvas.itemconfig(points, text=f"{POINTS}/{ATTEMPTED}")
    ATTEMPTED += 1
    flip_timer = windows.after(3000, func=flip_card)


def answered():
    global POINTS
    POINTS += 1
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr["English"], fill="white")
    canvas.itemconfig(front, image=card_back)


windows = Tk()
windows.configure(bg=BACKGROUND, padx=100, pady=100)
windows.title("Flashy")
flip_timer = windows.after(5000, func=flip_card)

right = PhotoImage(file=r"C:\Users\rahul\Desktop\python\demo\flash-card-project-start\images\right.png")
wrong = PhotoImage(file=r"C:\Users\rahul\Desktop\python\demo\flash-card-project-start\images\wrong.png")
card_front = PhotoImage(file=r"C:\Users\rahul\Desktop\python\demo\flash-card-project-start\images\card_front.png")
card_back = PhotoImage(file=r"C:\Users\rahul\Desktop\python\demo\flash-card-project-start\images\card_back.png")

canvas = Canvas(width=800, height=526)
front = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND, borderwidth=0, highlightthickness=0)
points = canvas.create_text(400, 450, text="0/0", font=("Arial", 30, 'bold'))
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

correct_button = Button(image=right, highlightthickness=0, padx=10, pady=20, command=answered)
correct_button.grid(row=3, column=0)

wrong_button = Button(image=wrong, highlightthickness=0, padx=10, pady=20, command=next_card)
wrong_button.grid(row=3, column=2)

next_card()

windows.mainloop()
