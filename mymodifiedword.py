import tkinter as tk
count = 0
def increment():
    global count
    count = count + 1
    number_label.config(text=f"Clicks: {count}")
window = tk.Tk()
window.title("Click Counter App")
window.geometry("300x200")
number_label = tk.Label(window, text="Clicks: 0", font=("Arial", 24))
number_label.pack(pady=20) 
click_button = tk.Button(window, text="Click Me!", command=increment, font=("Arial", 14))
click_button.pack()
window.mainloop()
