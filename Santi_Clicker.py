
import tkinter as tk


win = tk.Tk()
back1='#1A5990'
photo = tk.PhotoImage(file='icon.png')
win.title("Santi`s Clicker")
win.iconphoto(False, photo)
win.config(bg=back1)
win.geometry('500x500+600+150')
win.resizable(False, False)

def ydarm():
    global money
    ydarr = 1
    money += ydarr
    textm['text'] = f"Количество твоих денег: {money}"

money = 0

textm = tk.Label(win, text=f"Количество твоих денег: {money}",
                 font=('Comic Sans MS',15),
                 background=back1,
                 justify=tk.CENTER
                 )

textm.grid()

ydar = tk.Button(win, text='Нажми, чтобы ударить скрепку', command=ydarm)
                   
                 
ydar.grid(row=1, column=1)

win.mainloop()

