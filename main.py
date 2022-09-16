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
scorelbl = Label(window, text='Score', font=('Times New Roman', 16, 'bold', 'underline'))
win_scorelbl = Label(window, text='W')
tie_scorelbl = Label(window, text='T')
lose_scorelbl = Label(window, text='L')


board.grid(column=0,row=0)

window.mainloop()