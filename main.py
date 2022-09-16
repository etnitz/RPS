from calendar import c
from cgitb import text
import random
from tkinter import *

window = Tk()

window.geometry('1000x500')
window.title("Rock Paper Scissors")

content = Frame(window)
board = Frame(content, bg='blue', borderwidth=5, relief='ridge', width='500', height='500')
rock = Button(content, text='Rock', font=('Times New Roman', 12, 'bold'))
paper = Button(content, text='Paper', font=('Times New Roman', 12, 'bold'))
scissors = Button(content, text='scissors', font=('Times New Roman', 12, 'bold'))
score_lbl = Label(content, text='Score', font=('Times New Roman', 16, 'bold', 'underline'))
win_score_lbl = Label(content, text='W')
tie_score_lbl = Label(content, text='T')
lose_score_lbl = Label(content, text='L')
stats_lbl = Label(content, text='Stats', font=('Times New Roman', 16, 'bold', 'underline'))
win_per_lbl = Label(content, text='W')
tie_per_lbl = Label(content, text='T')
loss_per_lbl = Label(content, text='L')

content.grid(column=0,row=0)
board.grid(column=0,row=0, columnspan=4, rowspan=3)
score_lbl.grid(column=5,row=0, columnspan=3)
stats_lbl.grid(column=5, row=2, columnspan=3)
rock.grid(column=1, row=1)
paper.grid(column=2, row=1)
scissors.grid(column=3, row=1)
win_score_lbl.grid(column=5,row=1)
tie_score_lbl.grid(column=6,row=1)
lose_score_lbl.grid(column=7,row=1)
win_per_lbl.grid(column=5,row=3)
tie_per_lbl.grid(column=6,row=3)
loss_per_lbl.grid(column=7,row=3)

window.mainloop()