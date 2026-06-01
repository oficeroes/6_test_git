import tkinter as tk

def say_hello():
    print("你点击了按钮！")

def magic():
    var.set("change!")
root = tk.Tk()
root.geometry('300x200')


var = tk.StringVar()
var.set("hello")
label = tk.Label(root, textvariable=var, font=('Arial', 12))
label.pack(pady=20)

btn = tk.Button(root, text="点击见证奇迹", command=magic)
btn.pack()



root.mainloop()