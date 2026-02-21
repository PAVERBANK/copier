import tkinter as tk
import shutil as sh
import keyboard as ke 

root = tk.Tk()
root.title("kopyer")
root.geometry("600x700")
root.configure(bg="black")

btn11=True
def check_keys1():
    global btn11
    btn11=False
def xyita():
    if btn11==False:
            print("Цикл зупинено")
            return 
def check_keys():
    
    if ke.is_pressed("F1"):
        try:
            sh.copy(entry_field.get(), entry.get())
            print("Файл скопійовано!")
        except Exception as e:
            print(f"Помилка: {e}")
    
    try:
        xyita()
    except Exception as e:
        print("не вишло")

    

def start_loop():
    print("Моніторинг клавіш запущено")
    check_keys()
def start_loop1():
    print("Моніторинг клавіш зупинено")
    check_keys1()

btn = tk.Button(root, text="START", bg="grey", font=("Arial", 15), command=start_loop)
btn.place(x=50, y=100, width=150, height=40)

btn1 = tk.Button(root, text="STOP", bg="grey", font=("Arial", 15), command=start_loop1)
btn1.place(x=250, y=100, width=150, height=40)

from_var = tk.StringVar()  
to_var = tk.StringVar()     

entry_field = tk.Entry(root, textvariable=from_var)
entry_field.place(x=50, y=150, width=150, height=30)

entry = tk.Entry(root, textvariable=to_var)
entry.place(x=50, y=200, width=150, height=30)


root.mainloop()
