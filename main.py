import random
from tkinter import *
from tkinter import messagebox
import mysql.connector

def show():
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()
    myCur.execute('SELECT * FROM stats')
    stats = myCur.fetchall()
    for stat in stats:
        win_score.config(text=str(stat[1]))
        tie_score.config(text=str(stat[3]))
        lose_score.config(text=str(stat[2]))

    myDB.close()

def win_per():
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()
    myCur.execute('SELECT * FROM stats')
    stats = myCur.fetchall()
    
    for stat in stats:
        total = stat[1] + stat[2] + stat[3]
        wins = round((stat[1]/ total) * 100, 2)
        win_score_per.config(text=f'{wins}%')
    
    myDB.close()

def tie_per():
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()
    myCur.execute('SELECT * FROM stats')
    stats = myCur.fetchall()
    
    for stat in stats:
        total = stat[1] + stat[2] + stat[3]
        ties = round((stat[3]/ total) * 100, 2)
        tie_score_per.config(text=f'{ties}%')
    
    myDB.close()

def loss_per():
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()
    myCur.execute('SELECT * FROM stats')
    stats = myCur.fetchall()
    for stat in stats:
        total = stat[1] + stat[2] + stat[3]
        losses = round((stat[2]/ total) * 100, 2)
        loss_score_per.config(text=f'{losses}%')
    myDB.close()


def roca():
    player = 'r'
    comp = random.choice(['r', 'p', 's'])    
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()

# Tie statement
    if player == comp:
        messagebox.showinfo('Tie', "You both chose Rock")
        myCur.execute('UPDATE stats SET tie = tie + 1')
        myDB.commit()
# Win statment
    elif comp == 's':
        messagebox.showinfo('WIN!', 'You Win! Congratulations, Rock beats Scissors!')
        myCur.execute('UPDATE stats SET wins = wins + 1')
        myDB.commit()
# Lose statement
    else:
        messagebox.showwarning('Lose', 'Sorry, Paper beats Rock. Better luck next time!')
        myCur.execute('UPDATE stats SET loss = loss + 1')
        myDB.commit()
        
    show()
    win_per()
    tie_per()
    loss_per()
    myDB.close()

def papel():
    player = 'p'
    comp = random.choice(['r', 'p', 's'])
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()

# Tie statement
    if player == comp:
        messagebox.showinfo('Tie', "You both chose Paper")
        myCur.execute('UPDATE stats SET tie = tie + 1')
        myDB.commit()
# Win statment
    elif comp == 'r':
        messagebox.showinfo('WIN!', 'You Win! Congratulations, Paper beats Rock!')
        myCur.execute('UPDATE stats SET wins = wins + 1')
        myDB.commit()
# Lose statement
    else:
        messagebox.showwarning('Lose', 'Sorry, Scissors beats Paper. Better luck next time!')
        myCur.execute('UPDATE stats SET loss = loss + 1')
        myDB.commit()

    show()
    win_per()
    tie_per()
    loss_per()
    myDB.close()

def tijeras():
    player = 's'
    comp = random.choice(['r', 'p', 's'])
    myDB = mysql.connector.connect(host='localhost', user='root', password='password', database='rps_stats')
    myCur = myDB.cursor()

# Tie statement
    if player == comp:
        messagebox.showinfo('Tie', "You both chose Scissors")
        myCur.execute('UPDATE stats SET tie = tie + 1')
        myDB.commit()
# Win statment
    elif comp == 'p':
        messagebox.showinfo('WIN!', 'You Win! Congratulations, Scissors beats paper!')
        myCur.execute('UPDATE stats SET wins = wins + 1')
        myDB.commit()
# Lose statement
    else:
        messagebox.showwarning('Lose', 'Sorry, Rock beats Scissors. Better luck next time!')
        myCur.execute('UPDATE stats SET loss = loss + 1')
        myDB.commit()

    show()
    win_per()
    tie_per()
    loss_per()
    myDB.close()

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
win_score = Label(content)
tie_score = Label(content)
lose_score = Label(content)
stats_lbl = Label(content, text='Stats', font=('Times New Roman', 16, 'bold', 'underline'))
win_per_lbl = Label(content, text='W')
tie_per_lbl = Label(content, text='T')
loss_per_lbl = Label(content, text='L')
win_score_per = Label(content)
tie_score_per = Label(content)
loss_score_per = Label(content)
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
win_score.place(x=600, y=150)
tie_score.place(x=750, y=150)
lose_score.place(x=900, y=150)
stats_lbl.place(x=730, y=250)
win_per_lbl.place(x=600, y=300)
tie_per_lbl.place(x=750, y=300)
loss_per_lbl.place(x=900, y=300)
win_score_per.place(x=590, y=350)
tie_score_per.place(x=740, y=350)
loss_score_per.place(x=890, y=350)
delete_button.place(x=720, y=465)

show()
win_per()
tie_per()
loss_per()

window.mainloop()