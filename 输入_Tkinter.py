import tkinter as tk

def update_text():
    # 使用 .get() 获取输入框里的文字
    content = entry.get()
    # 将文字同步到标签上
    var.set(f"你输入的是：{content}")

root = tk.Tk()
root.geometry("300x150")

var = tk.StringVar()
var.set("在这里显示结果")

label = tk.Label(root, textvariable=var)
label.pack(pady=10)

# 1. 创建输入框 (Entry)
entry = tk.Entry(root)
entry.pack(pady=5)

# 2. 按钮触发获取文字的函数
btn = tk.Button(root, text="点击同步", command=update_text)
btn.pack()

root.mainloop()