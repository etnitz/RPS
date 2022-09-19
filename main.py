from calendar import c
from cgitb import text
import random
from tkinter import *

window = Tk()

window.geometry('1000x500')
window.title("Rock Paper Scissors")

content = Frame(window, width='1000', height='500')
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
delete_button = Button(content, text='Delete', bg='red')

window.resizable(False, False)
content.place(x=0, y=0)
board.place(x=0, y=0)
rock.place(x=100, y=230)
paper.place(x=200, y=230)
scissors.place(x=300, y=230)
score_lbl.place(x=730, y=50)
win_score_lbl.place(x=600, y=100)
tie_score_lbl.place(x=750, y=100)
lose_score_lbl.place(x=900, y=100)
stats_lbl.place(x=730, y=250)
win_per_lbl.place(x=600, y=300)
tie_per_lbl.place(x=750, y=300)
loss_per_lbl.place(x=900, y=300)
delete_button.place(x=720, y=465)

window.mainloop()