from tkinter import *
from tkinter import messagebox
import json

chosen_note = -1


# Обновление файла с данными
def rewrite_json():
    with open("note_file.json", "w") as outfile:
        json.dump(data, outfile)


# Добавление новой заметки
def new_note():
    entry_note = my_entry.get()
    if entry_note != "":
        lb.insert(END, entry_note)
        data['notes'].append(entry_note)
        my_entry.delete(0, "end")
        rewrite_json()
    else:
        messagebox.showwarning("warning", "Please enter some note.")


# Удаление заметки
def delete_note():
    if lb.curselection():
        del data['notes'][lb.curselection()[0]]
        lb.delete(lb.curselection()[0])
        rewrite_json()
    else:
        messagebox.showwarning("warning", "Please choose some note.")


# Редактирование заметки
def edit_note():
    global chosen_note
    if lb.curselection():
        my_entry.delete(0, "end")
        my_entry.insert(0, lb.get(ANCHOR))
        chosen_note = lb.curselection()[0]
    else:
        messagebox.showwarning("warning", "Please choose some note.")
        return
    lb.config(state=DISABLED)
    addNote_btn.config(state=DISABLED)
    delNote_btn.config(state=DISABLED)
    editNote_btn.config(state=DISABLED)
    saveNote_btn.config(state=NORMAL)


# Сохранение редактирования
def save_note():
    global chosen_note
    n_note = my_entry.get()
    if n_note != "":
        lb.config(state=NORMAL)
        lb.delete(chosen_note)
        lb.insert(chosen_note, n_note)
        data['notes'][chosen_note] = n_note
        my_entry.delete(0, "end")
        rewrite_json()
    else:
        messagebox.showwarning("warning", "Please enter some note.")
        return
    addNote_btn.config(state=NORMAL)
    delNote_btn.config(state=NORMAL)
    editNote_btn.config(state=NORMAL)
    saveNote_btn.config(state=DISABLED)


# Создание окна
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('PythonGuides')
ws.config(bg='#778899')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)
# Панель заметок
lb = Listbox(
    frame,
    width=35,
    height=8,
    font=('Calibri', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)
# Загрузка данных
f = open('note_file.json')
data = json.load(f)
for note in data['notes']:
    lb.insert(END, note)
f.close()

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
# Поле ввода
my_entry = Entry(
    ws,
    font=('times', 24),
    width=28
)

my_entry.pack(pady=20)
# Элементы управления
button_frame = Frame(ws)
button_frame.pack(pady=20, padx=20)

addNote_btn = Button(
    button_frame,
    text='Add Note',
    font=('Calibri', 14),
    bg='#32CD32',
    width=10,
    command=new_note
)
addNote_btn.pack(fill=BOTH, expand=True, side=LEFT)

delNote_btn = Button(
    button_frame,
    text='Delete Note',
    font=('Calibri', 14),
    bg='#F08080',
    width=10,
    command=delete_note
)
delNote_btn.pack(fill=BOTH, expand=True, side=LEFT)

editNote_btn = Button(
    button_frame,
    text='Edit Note',
    font=('Calibri', 14),
    bg='#FFD700',
    width=10,
    command=edit_note
)
editNote_btn.pack(fill=BOTH, expand=True, side=LEFT)

saveNote_btn = Button(
    button_frame,
    text='Save Note',
    font=('Calibri', 14),
    bg='#4682B4',
    state=DISABLED,
    width=10,
    command=save_note
)
saveNote_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
