import tkinter as tk
import shutil as sh
import keyboard as ke 

root = tk.Tk()
root.title("kopyer")
root.geometry("600x700")
root.configure(bg="black")

def check_keys():
    
    if ke.is_pressed("F1"):
        try:
            sh.copy(entry_field.get(), entry.get())
            print("Файл скопійовано!")
        except Exception as e:
            print(f"Помилка: {e}")
    
    
    if ke.is_pressed("F2"):
        print("Цикл зупинено")
        return 

    root.after(100, check_keys)

def start_loop():
    print("Моніторинг клавіш запущено...")
    check_keys()

btn = tk.Button(root, text="START", bg="grey", font=("Arial", 15), command=start_loop)
btn.place(x=50, y=100, width=150, height=40)
user_text = tk.StringVar()

from_var = tk.StringVar()   # звідки копіюємо
to_var = tk.StringVar()     # куди копіюємо

entry_field = tk.Entry(root, textvariable=from_var)
entry_field.place(x=50, y=150, width=150, height=30)

entry = tk.Entry(root, textvariable=to_var)
entry.place(x=50, y=200, width=150, height=30)


root.mainloop()
