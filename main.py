import random
from tkinter import *
from tkinter import messagebox

win_count = 0
tie_count = 0
loss_count = 0

def roca():
    global win_count
    global tie_count
    global loss_count
    player = 'r'
    comp = random.choice(['r', 'p', 's'])

# Tie statement
    if player == comp:
        messagebox.showinfo('Tie', "You both chose Rock")
        tie_count += 1
        print(comp)
# Win statment
    elif comp == 's':
        messagebox.showinfo('WIN!', 'You Win! Congratulations, Rock beats Scissors!')
        win_count += 1
        print(comp)
# Lose statement
    else:
        messagebox.showwarning('Lose', 'Sorry, Paper beats Rock. Better luck next time!')
        loss_count += 1
        print(comp)


def papel():
    global win_count
    global tie_count
    global loss_count
    player = 'p'
    comp = random.choice(['r', 'p', 's'])

# Tie statement
    if player == comp:
        messagebox.showinfo('Tie', "You both chose Paper")
        tie_count += 1
        print(comp)
# Win statment
    elif comp == 'r':
        messagebox.showinfo('WIN!', 'You Win! Congratulations, Paper beats Rock!')
        win_count += 1
        print(comp)
# Lose statement
    else:
        messagebox.showwarning('Lose', 'Sorry, Scissors beats Paper. Better luck next time!')
        loss_count += 1
        print(comp)

def tijeras():
    global win_count
    global tie_count
    global loss_count
    player = 's'
    comp = random.choice(['r', 'p', 's'])

# Tie statement
    if player == comp:
        messagebox.showinfo('Tie', "You both chose Scissors")
        tie_count += 1
        print(comp)
# Win statment
    elif comp == 'p':
        messagebox.showinfo('WIN!', 'You Win! Congratulations, Scissors beats paper!')
        win_count += 1
        print(comp)
# Lose statement
    else:
        messagebox.showwarning('Lose', 'Sorry, Rock beats Scissors. Better luck next time!')
        loss_count += 1
        print(comp)

window = Tk()

window.geometry('1000x500')
window.title("Rock Paper Scissors")

content = Frame(window, width='1000', height='500')
board = Frame(content, bg='blue', borderwidth=5, relief='ridge', width='500', height='500')
rock = Button(content, text='Rock', font=('Times New Roman', 12, 'bold'), command=roca)
paper = Button(content, text='Paper', font=('Times New Roman', 12, 'bold'), command=papel)
scissors = Button(content, text='Scissors', font=('Times New Roman', 12, 'bold'), command=tijeras)
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