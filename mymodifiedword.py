import tkinter as tk

# --- STEP 3: THE BRAIN (What happens when we click?) ---
count = 0
def increment():
    global count
    count = count + 1
    # Update the label text with the new number
    number_label.config(text=f"Clicks: {count}")


# --- STEP 1: THE WINDOW ---
window = tk.Tk()
window.title("Click Counter App")
window.geometry("300x200") # Sets the starting size of the window


# --- STEP 2: THE WIDGETS ---
# 1. A text label to show the number
number_label = tk.Label(window, text="Clicks: 0", font=("Arial", 24))
number_label.pack(pady=20) # pady adds some nice spacing around it

# 2. A button to click, wired to our 'increment' function
click_button = tk.Button(window, text="Click Me!", command=increment, font=("Arial", 14))
click_button.pack()


# --- STEP 4: OPEN THE DOORS ---
window.mainloop()