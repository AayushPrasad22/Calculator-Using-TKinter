import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except Exception:
            screen_var.set("Error")
            expresion = ""
    
    elif text == "C":
        expression = ""
        screen_var.set(expression)
    else:
        expression += text
        screen_var.set(expression)

root=tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

expression = ""
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar = screen_var, font = "Arial 20", bd=8, relief = "ridge", justify = "right" )
screen.pack(fill="both", ipadx=8, pady=10)

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill= "both")

    for btn in row:
        b= tk.Button(frame, text=btn, font="Arial 18", relief ="ridge", bd=4)
        b.pack(side="left", expand=True , fill="both")
        b.bind("<Button-1>",click)

root.mainloop()