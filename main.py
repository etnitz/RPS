from cgitb import text
import random
from tkinter import *

window = Tk()

window.geometry('1000x500')
window.title("Rock Paper Scissors")


board = Frame(window, bg='blue', borderwidth=5, relief='ridge', width='500', height='500')
rock = Button(window, text='Rock', font=('Times New Roman', 12, 'bold'))
paper = Button(window, text='Paper', font=('Times New Roman', 12, 'bold'))
scissors = Button(window, text='scissors', font=('Times New Roman', 12, 'bold'))
score_lbl = Label(window, text='Score', font=('Times New Roman', 16, 'bold', 'underline'))
win_score_lbl = Label(window, text='W')
tie_score_lbl = Label(window, text='T')
lose_score_lbl = Label(window, text='L')
statslbl = Label(window, text='Stats', font=('Times New Roman', 16, 'bold', 'underline'))
win_per_lbl = Label(window, text='W')
tie_per_lbl = Label(window, text='T')
loss_per_lbl = Label(window, text='L')


board.grid(column=0,row=0)

window.mainloop()