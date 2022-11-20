
import tkinter as tk
import time


win = tk.Tk()
back1='#1A5990'
photo = tk.PhotoImage(file='icon.png')
win.title("Santi`s Clicker")
win.iconphoto(False, photo)
win.config(bg=back1)
win.geometry('350x300+600+150')
win.resizable(False, False)

def noteno():
    note = tk.Label(win, text=f"У вас не хватает денег.",
                 font=('Comic Sans MS',10),
                 background=back1,
                 justify=tk.CENTER
                 )
    note.grid(row=7, column=0)
    note.after(1500, note.destroy)

def ydarm():
    ydar.config(state='disabled')
    global money
    money += ydarr
    textm['text'] = f"Количество твоих денег: {money}"
    ydar.after(1000, lambda: ydar.config(state='active'))

def proca1():
    global money
    global ydarr
    global lvl1
    global tsena1
    global intmoney
    global inttsena
    if money < tsena1:
        noteno()
    else:
        if lvl1 == 1:
            money -= tsena1
            lvl1 += 1
            tsena1 += 10
            ydarr += 1
            uluch1['text'] = f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}'
            textm['text'] = f"Количество твоих денег: {money}"
        elif lvl1 == 2:
            money -= tsena1
            lvl1 += 1
            tsena1 += 20
            ydarr += 2
            uluch1['text'] = f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}'
            textm['text'] = f"Количество твоих денег: {money}"
        elif lvl1 == 3:
            money -= tsena1
            lvl1 += 1
            tsena1 += 40
            ydarr += 3
            uluch1['text'] = f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}'
            textm['text'] = f"Количество твоих денег: {money}"
        elif lvl1 == 4:
            money -= tsena1
            lvl1 += 1
            tsena1 += 70
            ydarr += 4
            uluch1['text'] = f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}'
            textm['text'] = f"Количество твоих денег: {money}"
        elif lvl1 == 5:
            money -= tsena1
            lvl1 += 1
            ydarr += 5
            tsena1 += 100
            uluch1['text'] = f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}'
            textm['text'] = f"Количество твоих денег: {money}"
        elif lvl1 > 5:
            money -= tsena1
            lvl1 += 1
            ydarr += 10
            tsena1 += 150
            uluch1['text'] = f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}'
            textm['text'] = f"Количество твоих денег: {money}"


tsena1 = 10
lvl1 = 1
money = 0
ydarr = 1
intmoney = int(money)
inttsena = int(tsena1)

textm = tk.Label(win, text=f"Количество твоих денег: {money}",
                 font=('Comic Sans MS',15),
                 background=back1,
                 justify=tk.CENTER
                 )

textm.grid()

ydar = tk.Button(win, text='Нажми, чтобы ударить скрепку', command=ydarm, font=('Comic Sans MS',12), bg='#1AA61F')
uluch1 = tk.Button(win, text=f'Улучшить скрепку\nLvl - {lvl1}\nЦена - {tsena1}', command=proca1, font=('Comic Sans MS',10), bg='#971B1B', justify=tk.CENTER)
uluch1.grid(row=2, column=0, columnspan=1)
ydar.grid(row=1, column=0)

win.mainloop()

